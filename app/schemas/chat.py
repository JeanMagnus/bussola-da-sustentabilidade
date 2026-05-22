from pydantic import BaseModel, Field
from typing import Literal, Any


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
 

class ReferentValue(BaseModel):
    value:str = Field(description="Valor textual da entidade ou item referenciado.")
    attributes: dict[str, Any] = Field(
        default_factory = dict,
        description = "Atributos associados, se existirem. Ex: estado, ano, tema, nota, código, posição no ranking..."
    )

class ReferentGroup(BaseModel):
    label: str = Field(
        description = "Nome genérico do grupo referencido. Ex: cidades, critérios, temas, anos, destinos, indicadores."
    )
    kind_hint: str = Field(
        default = "unknown",
        description = "Tipo provável dos itens. Ex: cidade, estado, critério, tema, indicador, ano, município, ranking_item."
    )
    values: list[ReferentValue] = Field(
        default_factory = list,
        description = "Itens concretos que devem ser preservados."
    )
    expected_count: int | None = Field(
        default = None,
        description = "Quantidade esperada de itens neste grupo."
    )
    source: Literal["last_ai_message", "last_sql_result", "summary", "user_message"] = Field(
        default = "last_ai_message",
        description = "De onde esses referentes foram extraídos."
    )
    must_preserve: bool = Field(
        default = True,
        description = "Se true, o agente SQL não pode substituir esses itens por um filtro genérico."
    ) 

class ContextResolution(BaseModel):
    is_context_dependent: bool = Field(
        description = "True se a pergunta atual depende do contexto anterior."
    )
    rewritten_question: str = Field(
        description = "Pergunta reescrita de forma completa, sem depender de 'essas', 'eles', 'delas', etc."
    )
    referents: list[ReferentGroup] = Field(
        default_factory = list,
        description="Grupos genéricos de entidades ou itens do contexto anterior que precisam ser preservados."
    )
    requested_outputs: list[str] = Field(
        default_factory = list,
        description="Campos ou informações que o usuário quer obter. Ex: código IBGE, região, média, nota, ranking."
    ) 
    operation: str = Field(
        default="unknown",
        description="Operação principal: listar, contar, comparar, ranquear, filtrar, detalhar, agregar."
    )
    search_query: str = Field(
        description="Consulta curta para recuperar metadados no dicionário vetorial."
    )