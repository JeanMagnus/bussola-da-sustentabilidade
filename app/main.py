from fastapi import FastAPI
from contextlib import asynccontextmanager
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
from app.core.config import settings
from app.agent.graph import workflow
from app.routes import chat


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with AsyncPostgresSaver.from_conn_string(settings.URI_DATABASE_CHECKPOIN) as checkpointer:
        await checkpointer.setup()

        app.state.graph = workflow.compile(checkpointer=checkpointer)
        yield

app = FastAPI(lifespan=lifespan)
app.include_router(chat.router, tags=["Chat"])

@app.get("/", tags=["Health"])
async def root():
    return {"status": "online", "message": "Tá vivo!!"}