import asyncio
import json
import re
from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from app.schemas.chat import ChatInput, ChatOutput, StreamInput
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from time import perf_counter
from uuid import uuid4

router = APIRouter()
STREAMING_SPEED = 0.03

@router.post("/chat", response_model=ChatOutput)
async def chat_endpoint(request: ChatInput, req: Request):
    graph = req.app.state.graph

    started_at = perf_counter()

    config = {"configurable": {"recursion_limit": 15, "thread_id": request.thread_id, "user_id": request.user_id}}
    inputs = {"messages": [HumanMessage(content=request.message)]}

    result = await graph.ainvoke(inputs, config)
    last_msg = result["messages"][-1].content


    prompt_t = result.get("input_tokens", 0)
    output_t = result.get("output_tokens", 0)
    total_t = result.get("total_tokens", 0)

    print(f"TOKENS USADOS NO FLUXO /chat (thread_id={request.thread_id}, user_id={request.user_id}):")
    print(f"   |-- Entrada (Prompt): {prompt_t}")
    print(f"   |-- Saída (Geração): {output_t}")
    print(f"   |-- Total do fluxo: {total_t}")
    
    elapsed_seconds = perf_counter() - started_at
    print(f"LATENCY /chat: {elapsed_seconds:.2f}s (thread_id={request.thread_id}, user_id={request.user_id})")

    return ChatOutput(response=last_msg, thread_id=request.thread_id, user_id=request.user_id)

NODE_STATUS_MESSAGES = {
    "setup_node": "Preparando o contexto da conversa...",
    "summarization_node": "Resumindo o histórico da conversa...",
    "guardrail_input": "Verificando se a pergunta está dentro do escopo...",
    "classify_intent": "Identificando o tipo de análise necessária...",
    "dictionary_retrieval": "O agente está elaborando um dicionário para consulta...",
    "agent": "O agente está escrevendo e analisando a consulta...",
    "verify_sql": "O agente está validando a busca SQL...",
    "go_tools": "O agente está executando a consulta no banco de dados...",
    "moderation_output": "O agente está revisando a resposta final...",
}


def _message_to_dict(message: BaseMessage) -> dict:
    d = message.model_dump()
    d["type"] = message.type
    return d


def _sse(event: str, data) -> str:
    """
    Formato que o useStream espera:

    Formato:
        event: messages
        data: [...]

        event: custom
        data: {...}
    """
    payload = json.dumps(data, ensure_ascii=False, default=str)
    return f"event: {event}\ndata: {payload}\n\n"


def _extract_last_user_content(messages: list) -> str:
    for msg in reversed(messages):
        if not isinstance(msg, dict):
            continue

        role = msg.get("role") or msg.get("type")

        if role in ("user", "human"):
            return msg.get("content", "")

    if messages and isinstance(messages[-1], dict):
        return messages[-1].get("content", "")

    return ""


def _extract_visible_messages(messages: list) -> list:
    visible = []

    for msg in messages:
        msg_type = getattr(msg, "type", None)

        if msg_type in ("human", "ai"):
            visible.append(_message_to_dict(msg))

    return visible

def _get_message_content(message) -> str:
    """
    Extrai conteúdo textual de mensagens LangChain ou dicts.
    """
    if message is None:
        return ""

    if isinstance(message, dict):
        content = message.get("content", "")
    else:
        content = getattr(message, "content", "")

    if isinstance(content, str):
        return content.strip()

    if isinstance(content, list):
        parts = []

        for block in content:
            if isinstance(block, dict):
                if block.get("type") == "text":
                    parts.append(block.get("text", ""))
                elif "text" in block:
                    parts.append(block.get("text", ""))

        return "\n".join(parts).strip()

    return str(content).strip() if content else ""


def _has_tool_calls(message) -> bool:
    """
    Verifica se uma mensagem possui tool calls.
    """
    if message is None:
        return False

    if isinstance(message, dict):
        return bool(
            message.get("tool_calls")
            or message.get("tool_call_chunks")
            or message.get("additional_kwargs", {}).get("tool_calls")
        )

    return bool(
        getattr(message, "tool_calls", None)
        or getattr(message, "tool_call_chunks", None)
        or getattr(message, "additional_kwargs", {}).get("tool_calls", None)
    )


def _is_ai_message(message) -> bool:
    """
    Verifica se a mensagem é AIMessage ou dict equivalente.
    """
    if isinstance(message, AIMessage):
        return True

    if isinstance(message, dict):
        msg_type = message.get("type") or message.get("role")
        return msg_type in ("ai", "assistant")

    return getattr(message, "type", None) == "ai"


def _get_final_ai_content(state_values: dict) -> str:
    """
    Busca a resposta final real do grafo.

    Ordem:
    1. final_response, se existir no state;
    2. última AIMessage sem tool_calls;
    3. fallback controlado.
    """
    final_response = state_values.get("final_response")

    if isinstance(final_response, str) and final_response.strip():
        return final_response.strip()

    last_msg_ai = state_values.get("last_msg_ai")

    if isinstance(last_msg_ai, str) and last_msg_ai.strip():
        return last_msg_ai.strip()

    messages = state_values.get("messages", [])

    for msg in reversed(messages):
        if not _is_ai_message(msg):
            continue

        if _has_tool_calls(msg):
            continue

        content = _get_message_content(msg)

        if content:
            return content

    return (
        "Não consegui gerar uma resposta final adequada. "
        "Tente reformular sua pergunta."
    )

def _split_text_for_streaming(text: str) -> list[str]:
    """
    Divide a resposta em pequenos blocos preservando espaços.
    Isso simula streaming token a token de forma visualmente fluida.
    """
    if not text:
        return []

    chunks = re.findall(r"\S+\s*", text)

    return chunks if chunks else [text]


@router.post("/chat/stream")
async def chat_stream_endpoint(req: Request):
    """
    Endpoint compatível com useStream + FetchStreamTransport.

    Mantém:
      - status do agente em streaming
      - stop pelo frontend
      - fallback de resposta final

    Importante:
      - não envia texto intermediário do agent;
      - envia apenas a resposta final ao término do grafo.
    """

    graph = req.app.state.graph
    body = await req.json()

    input_data = body.get("input") or body.get("inputs") or {}
    config_data = body.get("config") or {}
    configurable = config_data.get("configurable") or {}

    raw_messages = input_data.get("messages") or body.get("messages") or []

    user_content = (
        _extract_last_user_content(raw_messages)
        or body.get("message")
        or ""
    )

    thread_id = (
        configurable.get("thread_id")
        or body.get("thread_id")
        or body.get("threadId")
        or "default"
    )

    user_id = (
        configurable.get("user_id")
        or body.get("user_id")
        or body.get("userId")
        or "anonymous"
    )

    config = {
        "recursion_limit": 100,
        "configurable": {
            "thread_id": thread_id,
            "user_id": user_id,
        },
    }

    inputs = {
        "messages": [
            HumanMessage(content=user_content)
        ]
    }

    async def event_generator():
        yield _sse(
            "metadata",
            {
                "run_id": f"run-{thread_id}",
                "thread_id": thread_id,
            },
        )

        try:
            last_status_node = None
            message_id = f"assistant-{thread_id}-{uuid4()}"

            async for chunk in graph.astream(
                inputs,
                config=config,
                stream_mode=["messages", "updates"],
                version="v2",
            ):
                stream_type = chunk["type"]
                data = chunk["data"]

                if stream_type == "updates":
                    if isinstance(data, dict):
                        for node_name in data.keys():
                            status_message = NODE_STATUS_MESSAGES.get(node_name)

                            if status_message and node_name != last_status_node:
                                last_status_node = node_name

                                yield _sse(
                                    "custom",
                                    {
                                        "type": "status",
                                        "node": node_name,
                                        "message": status_message,
                                    },
                                )

                    continue

                if stream_type == "messages":
                    message_chunk, metadata = data
                    node_name = metadata.get("langgraph_node")

                    if node_name != "agent":
                        continue

                    additional_kwargs = getattr(message_chunk, "additional_kwargs", {}) or {}

                    if "reasoning_content" in additional_kwargs:
                        reasoning = additional_kwargs.get("reasoning_content", "")

                        if reasoning:
                            yield _sse(
                                "custom",
                                {
                                    "type": "thinking",
                                    "content": reasoning,
                                },
                            )

                    if (
                        hasattr(message_chunk, "content_blocks")
                        and message_chunk.content_blocks
                    ):
                        for block in message_chunk.content_blocks:
                            if block.get("type") == "reasoning":
                                reasoning = block.get("reasoning", "")

                                if reasoning:
                                    yield _sse(
                                        "custom",
                                        {
                                            "type": "thinking",
                                            "content": reasoning,
                                        },
                                    )

                    continue

            state = await graph.aget_state(config)
            final_content = _get_final_ai_content(state.values)

            yield _sse(
                "custom",
                {
                    "type": "status",
                    "node": "final_response",
                    "message": "Escrevendo resposta final...",
                },
            )

            for text_chunk in _split_text_for_streaming(final_content):
                yield _sse(
                    "messages",
                    [
                        {
                            "type": "ai",
                            "id": message_id,
                            "content": text_chunk,
                        },
                        {
                            "langgraph_node": "agent",
                            "tags": ["resposta_final"],
                        },
                    ],
                )

                await asyncio.sleep(STREAMING_SPEED)

            yield _sse(
                "custom",
                {
                    "type": "done",
                },
            )

        except Exception as exc:
            print(f"[SSE] Erro durante streaming: {exc}")

            yield _sse(
                "error",
                {
                    "message": str(exc),
                    "type": exc.__class__.__name__,
                },
            )

            yield _sse(
                "custom",
                {
                    "type": "done",
                },
            )

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
            "Connection": "keep-alive",
        },
    )