import json
import asyncio
from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from app.schemas.chat import ChatInput, ChatOutput, StreamInput
from app.core.config import settings
from langchain_core.messages import HumanMessage, AIMessageChunk, AIMessage
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
from time import perf_counter

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


@router.post("/chat/stream")
async def chat_stream_endpoint(request: StreamInput, req: Request):
    """
    Emite Server-Sent Events no formato esperado pelo useStream do LangChain.
 
    Cada linha é um objeto JSON com os campos:
        { "event": "<tipo>", "data": { ... } }
 
    Eventos emitidos:
        messages/partial  — fragmento de mensagem enquanto o LLM escreve
        messages/complete — mensagem final completa (AIMessage)
        metadata          — metadados do run (run_id, thread_id)
        error             — qualquer exceção não tratada
    """
 
    graph = req.app.state.graph
 
    config = {
        "configurable": {
            "recursion_limit": 15,
            "thread_id": request.thread_id,
            "user_id": request.user_id,
        }
    }
    inputs = {"messages": [HumanMessage(content=request.message)]}
 
    async def event_generator():
        # ── 1. Metadados iniciais ──────────────────────────────────────────
        yield _sse(
            "metadata",
            {
                "run_id": f"run-{request.thread_id}",
                "thread_id": request.thread_id,
            },
        )
 
        accumulated_content = ""
 
        try:
            # ── 2. Stream token a token via astream_events ─────────────────
            async for event in graph.astream_events(inputs, config, version="v2"):
                kind = event.get("event", "")
 
                # Captura fragmentos gerados pelo LLM (on_chat_model_stream)
                if kind == "on_chat_model_stream":
                    chunk = event.get("data", {}).get("chunk")
                    if isinstance(chunk, AIMessageChunk) and chunk.content:
                        token = chunk.content
                        accumulated_content += token
 
                        # Envia o fragmento parcial para o frontend atualizar
                        # o estado em tempo real
                        yield _sse(
                            "messages/partial",
                            [
                                {
                                    "type": "ai",
                                    "content": accumulated_content,
                                    "id": f"msg-{request.thread_id}",
                                }
                            ],
                        )
 
                        # Pequena pausa para não sobrecarregar o cliente
                        await asyncio.sleep(0)
 
            # ── 3. Mensagem completa após o grafo terminar ─────────────────
            if accumulated_content:
                yield _sse(
                    "messages/complete",
                    [
                        {
                            "type": "ai",
                            "content": accumulated_content,
                            "id": f"msg-{request.thread_id}",
                        }
                    ],
                )
 
        except Exception as exc:
            print(f"[SSE] Erro durante streaming: {exc}")
            yield _sse("error", {"message": str(exc)})
 
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            # Impede que proxies e navegadores façam cache do stream
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
            # Necessário para que o FetchStreamTransport leia o stream
            "Access-Control-Allow-Origin": "*",
        },
    )
 
 
# ─────────────────────────────────────────────
# Utilitário interno
# ─────────────────────────────────────────────
def _sse(event: str, data) -> str:
    """
    Serializa um evento SSE no formato ndjson esperado pelo LangChain SDK.
 
    Formato:
        data: {"event": "...", "data": ...}\n\n
    """
    payload = json.dumps({"event": event, "data": data}, ensure_ascii=False)
    return f"data: {payload}\n\n"