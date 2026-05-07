from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
from app.core.config import settings
from app.agent.graph import workflow
from app.routes import chat, reports


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with AsyncPostgresSaver.from_conn_string(settings.URI_DATABASE_CHECKPOIN) as checkpointer:
        await checkpointer.setup()

        app.state.graph = workflow.compile(checkpointer=checkpointer)

        try:
            print("Tentando gerar imagem do grafo...")
            graph_png = app.state.graph.get_graph().draw_mermaid_png()
            
            with open("grafo_projeto_bussola.png", "wb") as f:
                f.write(graph_png)
            print("Grafo salvo com sucesso!")
        except Exception as e:
            print(f"Aviso: Não foi possível gerar a imagem do grafo (Timeout ou Rede).")
            print(f"Dica: O sistema continuará funcionando normalmente sem a imagem.")
        yield

app = FastAPI(lifespan=lifespan)
app.include_router(chat.router, tags=["Chat"])
app.include_router(reports.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Health"])
async def root():
    return {"status": "online", "message": "Tá vivo!!"}

