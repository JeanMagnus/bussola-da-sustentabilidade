import json
from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from app.schemas.chat import ChatInput, ChatOutput, StreamInput
from langchain_core.messages import HumanMessage, AIMessage
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
    Emite Server-Sent Events para o frontend.

    Importante: para evitar "poluição" da resposta com tokens intermediários
    de nós internos do grafo, este endpoint envia apenas a mensagem final
    do agente em `messages/complete`.
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
        yield _sse(
            "metadata",
            {
                "run_id": f"run-{request.thread_id}",
                "thread_id": request.thread_id,
            },
        )

        try:
            streamed_content = False
            async for event in graph.astream_events(inputs, config, version="v2"):
            
                if event["event"] == "on_chat_model_stream":

                    tags = event.get("tags", [])

                    if "resposta_final" in tags:
                        chunk = event["data"]["chunk"]

                        if hasattr(chunk, "content_blocks") and chunk.content_blocks:
                            for block in chunk.content_blocks:
                                if block.get("type") == "reasoning":
                                    yield _sse("thinking", {"content": block["reasoning"]})
                                elif block.get("type") == "text":
                                    streamed_content = True
                                    yield _sse("chunk", {"content": block["text"]})
                        
                        elif chunk.content and getattr(chunk, "tool_call_chunks", None):
                            yield _sse("thinking", {"content": chunk.content})

                        elif chunk.content and not getattr(chunk, "tool_call_chunks", None):
                            streamed_content = True
                            yield _sse("chunk", {"content": chunk.content})
                
                elif event["event"] == "on_tool_start":
                    yield _sse("status", {"message": f"Executando {event['name']}..."})

            state = await graph.aget_state(config)
            final_messages = state.values.get("messages", [])
            
            if final_messages:
                last_msg = final_messages[-1]
                
                if not streamed_content and isinstance(last_msg, AIMessage):
                    yield _sse("chunk", {"content": last_msg.content})

            yield _sse(
                "messages/complete",
                [
                    {
                        "type": "ai",
                        "status": "done"
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
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
            "Access-Control-Allow-Origin": "*",
            "Connection": "keep-alive"
        },
    )

def _sse(event: str, data) -> str:
    """
    Serializa um evento SSE no formato ndjson esperado pelo LangChain SDK.
 
    Formato:
        data: {"event": "...", "data": ...}\n\n
    """
    payload = json.dumps({"event": event, "data": data}, ensure_ascii=False)
    return f"data: {payload}\n\n"