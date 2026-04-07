from fastapi import APIRouter, Request
from app.schemas.chat import ChatInput, ChatOutput
from app.core.config import settings
from langchain_core.messages import HumanMessage
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
