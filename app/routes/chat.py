from fastapi import APIRouter, Request
from app.schemas.chat import ChatInput, ChatOutput
from app.core.config import settings
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver

router = APIRouter()

@router.post("/chat", response_model=ChatOutput)
async def chat_endpoint(request: ChatInput, req: Request):
    graph = req.app.state.graph

    config = {"configurable": {"recursion_limit": 15,"thread_id": request.thread_id, "user_id": request.user_id}}
    inputs = {"messages": [HumanMessage(content=request.message)]}

    result = await graph.ainvoke(inputs, config)
    last_msg = result["messages"][-1].content

    return ChatOutput(response=last_msg, thread_id=request.thread_id, user_id=request.user_id)
