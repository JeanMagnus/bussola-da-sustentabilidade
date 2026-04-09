from pydantic import BaseModel, Field
from typing import Literal


# Models do fastapi para entrada e saída de dados
class ChatInput(BaseModel):
    message: str
    thread_id: str = "default"
    user_id: str = "anonymous"

class ChatOutput(BaseModel):
    response: str
    thread_id: str
    user_id: str

class IntentRouter(BaseModel):
    reasoning: str = Field(
        description="Explique passo a passo se o usuário está pedindo dados específicos"
                    "(métricas, cidades, rankings) ou se é uma pergunta geral/saudação."
    )
    intent: Literal["SQL", "CONVERSA"] = Field(
        description="O veredito final. Use 'SQL' para busca de dados e 'CONVERSA' para chat geral."
    )
    
    