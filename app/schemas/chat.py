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
    is_continuation: str = Field(
        description="Responda 'SIM' se a pergunta atual depender do contexto da mensagem anterior (ex: usa pronomes como 'elas', 'dessas', 'e no estado X?'). Responda 'NAO' se for um assunto novo."
    )
    
class KeywordExtraction(BaseModel):
    search_query: str = Field(description="Uma string contendo 3 a 6 palavras-chave minúsculas, separadas por espaço, essenciais para a busca no banco de dados. Nunca deve estar vazia. Exemplo: 'cidades turismo sustentabilidade ibge'.")


class StreamInput(BaseModel):
    """
    Entrada para o endpoint de streaming /chat/stream.
    Idêntica ao ChatInput — separada para clareza semântica e
    para permitir extensões futuras específicas ao stream.
    """
    message: str
    thread_id: str = "default"
    user_id: str = "anonymous"
 