import json
from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from app.schemas.chat import ChatInput, ChatOutput, StreamInput
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from time import perf_counter
from uuid import uuid4

router = APIRouter()

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


# @router.post("/chat/stream")
# async def chat_stream_endpoint(request: StreamInput, req: Request):
#     """
#     Emite Server-Sent Events para o frontend.

#     Importante: para evitar "poluição" da resposta com tokens intermediários
#     de nós internos do grafo, este endpoint envia apenas a mensagem final
#     do agente em `messages/complete`.
#     """

#     graph = req.app.state.graph

#     config = {
#         "configurable": {
#             "recursion_limit": 15,
#             "thread_id": request.thread_id,
#             "user_id": request.user_id,
#         }
#     }
#     inputs = {"messages": [HumanMessage(content=request.message)]}

#     async def event_generator():
#         yield _sse(
#             "metadata",
#             {
#                 "run_id": f"run-{request.thread_id}",
#                 "thread_id": request.thread_id,
#             },
#         )

#         try:
#             streamed_content = False
#             async for event in graph.astream_events(inputs, config, version="v2"):
            
#                 if event["event"] == "on_chat_model_stream":

#                     tags = event.get("tags", [])

#                     if "resposta_final" in tags:
#                         chunk = event["data"]["chunk"]

#                         if hasattr(chunk, "content_blocks") and chunk.content_blocks:
#                             for block in chunk.content_blocks:
#                                 if block.get("type") == "reasoning":
#                                     yield _sse("thinking", {"content": block["reasoning"]})
#                                 elif block.get("type") == "text":
#                                     streamed_content = True
#                                     yield _sse("chunk", {"content": block["text"]})
                        
#                         elif chunk.content and getattr(chunk, "tool_call_chunks", None):
#                             yield _sse("thinking", {"content": chunk.content})

#                         elif chunk.content and not getattr(chunk, "tool_call_chunks", None):
#                             streamed_content = True
#                             yield _sse("chunk", {"content": chunk.content})
                
#                 elif event["event"] == "on_tool_start":
#                     yield _sse("status", {"message": f"Executando {event['name']}..."})

#             state = await graph.aget_state(config)
#             final_messages = state.values.get("messages", [])
            
#             if final_messages:
#                 last_msg = final_messages[-1]
                
#                 if not streamed_content and isinstance(last_msg, AIMessage):
#                     yield _sse("chunk", {"content": last_msg.content})

#             yield _sse(
#                 "messages/complete",
#                 [
#                     {
#                         "type": "ai",
#                         "status": "done"
#                     }
#                 ],
#             )

#         except Exception as exc:
#             print(f"[SSE] Erro durante streaming: {exc}")
#             yield _sse("error", {"message": str(exc)})

#     return StreamingResponse(
#         event_generator(),
#         media_type="text/event-stream",
#         headers={
#             "Cache-Control": "no-cache",
#             "X-Accel-Buffering": "no",
#             "Access-Control-Allow-Origin": "*",
#             "Connection": "keep-alive"
#         },
#     )

# NODE_STATUS_MESSAGES = {
#     "setup_node": "Preparando o contexto da conversa...",
#     "summarization_node": "Resumindo o histórico da conversa...",
#     "guardrail_input": "Verificando se a pergunta está dentro do escopo...",
#     "classify_intent": "Identificando o tipo de análise necessária...",
#     "dictionary_retrieval": "O agente está elaborando um dicionário para consulta...",
#     "agent": "O agente está escrevendo e analisando a consulta...",
#     "verify_sql": "O agente está validando a busca SQL...",
#     "go_tools": "O agente está executando a consulta no banco de dados...",
#     "moderation_output": "O agente está revisando a resposta final...",
# }

# @router.post("/chat/stream")
# async def chat_stream_endpoint(request: StreamInput, req: Request):
#     """
#     Emite Server-Sent Events para o frontend.

#     Versão usando graph.astream em vez de graph.astream_events.
#     Mantém o mesmo protocolo atual do frontend:
#       - metadata
#       - chunk
#       - thinking
#       - status
#       - messages/complete
#       - error
#     """

#     graph = req.app.state.graph

#     config = {
#         "configurable": {
#             "recursion_limit": 15,
#             "thread_id": request.thread_id,
#             "user_id": request.user_id,
#         }
#     }

#     inputs = {
#         "messages": [
#             HumanMessage(content=request.message)
#         ]
#     }

#     async def event_generator():
#         yield _sse(
#             "metadata",
#             {
#                 "run_id": f"run-{request.thread_id}",
#                 "thread_id": request.thread_id,
#             },
#         )

#         try:
#             streamed_content = False
#             last_status_node = None 

#             async for chunk in graph.astream(
#                 inputs,
#                 config=config,
#                 stream_mode=["messages", "updates"],
#                 version="v2",
#             ):
#                 stream_type = chunk["type"]
#                 data = chunk["data"]
#                 if stream_type == "updates":
#                     if isinstance(data, dict):
#                         for node_name in data.keys():
#                             status_message = NODE_STATUS_MESSAGES.get(node_name)

#                             if status_message and node_name != last_status_node:
#                                 last_status_node = node_name

#                                 yield _sse(
#                                     "status",
#                                     {
#                                         "node": node_name,
#                                         "message": status_message,
#                                     },
#                                 )
                            
#                     continue

#                 if stream_type == "messages":
#                     message_chunk, metadata = data

#                     tags = metadata.get("tags", [])

#                     # Mantém a mesma lógica que você tinha:
#                     # só transmite a resposta final marcada com "resposta_final".
#                     if "resposta_final" not in tags:
#                         continue

#                     # Caso o modelo retorne content_blocks.
#                     if (
#                         hasattr(message_chunk, "content_blocks")
#                         and message_chunk.content_blocks
#                     ):
#                         for block in message_chunk.content_blocks:
#                             if block.get("type") == "reasoning":
#                                 continue

#                             elif block.get("type") == "text":
#                                 content = block.get("text", "")
#                                 if content:
#                                     streamed_content = True
#                                     yield _sse(
#                                         "chunk",
#                                         {"content": content},
#                                     )
                            
#                     else:
#                         if getattr(message_chunk, "tool_call_chunks", None):
#                             continue

#                         content = getattr(message_chunk, "content", "")

#                         if content:
#                             streamed_content = True
#                             yield _sse(
#                                 "chunk",
#                                 {"content": content},
#                             )

#                 elif stream_type == "updates":
#                     # Com astream você não recebe "on_tool_start" diretamente.
#                     # Aqui dá para emitir status com base nos nós atualizados.
#                     updates = data

#                     if isinstance(updates, dict):
#                         for node_name in updates.keys():
#                             if node_name in ("go_tools", "tools", "tool_node"):
#                                 yield _sse(
#                                     "status",
#                                     {"message": f"Executando Ferramentas..."},
#                                 )

#             state = await graph.aget_state(config)
#             final_messages = state.values.get("messages", [])

#             if final_messages:
#                 last_msg = final_messages[-1]

#                 if not streamed_content and isinstance(last_msg, AIMessage):
#                     yield _sse(
#                         "chunk",
#                         {"content": last_msg.content},
#                     )

#             yield _sse(
#                 "messages/complete",
#                 [
#                     {
#                         "type": "ai",
#                         "status": "done",
#                     }
#                 ],
#             )

#         except Exception as exc:
#             print(f"[SSE] Erro durante streaming: {exc}")
#             yield _sse("error", {"message": str(exc)})

#     return StreamingResponse(
#         event_generator(),
#         media_type="text/event-stream",
#         headers={
#             "Cache-Control": "no-cache",
#             "X-Accel-Buffering": "no",
#             "Access-Control-Allow-Origin": "*",
#             "Connection": "keep-alive",
#         },
#     )


# def _sse(event: str, data) -> str:
#     """
#     Serializa um evento SSE no formato ndjson esperado pelo LangChain SDK.
 
#     Formato:
#         data: {"event": "...", "data": ...}\n\n
#     """
#     payload = json.dumps({"event": event, "data": data}, ensure_ascii=False)
#     return f"data: {payload}\n\n"

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


@router.post("/chat/stream")
async def chat_stream_endpoint(req: Request):
    """
    Endpoint compatível com useStream + FetchStreamTransport.

    Mantém:
      - resposta em streaming
      - status do agente
      - thinking
      - stop pelo frontend
      - fallback de resposta final
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
        "recursion_limit": 50,
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
            streamed_content = False
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
                    tags = metadata.get("tags", [])
                    node_name = metadata.get("langgraph_node")

                    # printar apenas mensagem final
                    if node_name != "agent":
                        continue

                    if "resposta_final" not in tags:
                        continue
                    
                    # ignorar tool calls na saída
                    if getattr(message_chunk, "tool_call_chunks", None):
                        continue

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

                            elif block.get("type") == "text":
                                text = block.get("text", "")

                                if text:
                                    streamed_content = True

                                    yield _sse(
                                        "messages",
                                        [
                                            {
                                                "type": "ai",
                                                "id": message_id,
                                                "content": text,
                                            },
                                            metadata,
                                        ],
                                    )

                    else:
                        content = getattr(message_chunk, "content", "")

                        if content:
                            streamed_content = True

                            yield _sse(
                                "messages",
                                [
                                    {
                                        "type": "ai",
                                        "id": message_id,
                                        "content": content,
                                    },
                                    metadata,
                                ],
                            )

            state = await graph.aget_state(config)
            final_messages = state.values.get("messages", [])

            if final_messages:
                last_msg = final_messages[-1]

                if not streamed_content and isinstance(last_msg, AIMessage):
                    yield _sse(
                        "messages",
                        [
                            {
                                "type": "ai",
                                "id": message_id,
                                "content": last_msg.content,
                            },
                            {
                                "langgraph_node": "agent",
                                "tags": ["resposta_final"],
                            },
                        ],
                    )

                # yield _sse(
                #     "values",
                #     {
                #         "messages": _extract_visible_messages(final_messages)
                #     },
                # )

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

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
            "Connection": "keep-alive",
        },
    )


# @router.post("/chat/stream_alt")
# async def chat_stream_alt_endpoint(request: StreamInput, req: Request):

