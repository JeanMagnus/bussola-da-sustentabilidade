from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langgraph.prebuilt import ToolNode
from langchain_core.runnables import RunnableConfig
from langchain_core.documents import Document
from langchain_core.tools import tool
from typing import Annotated, List, Literal
from app.core.config import model, db_bussola
from app.agent.memory import vector_store, Memory, guide_vector_store


@tool
async def store_memory_tool(
        memories: Annotated[List[Memory], "Lista de memórias a serem armazenadas"],
        config: RunnableConfig
) -> str:
    
    """Armazena memórias de longo prazo no banco vetorial Pinecone.

    Esta ferramenta permite registrar informações importantes sobre o usuário ou contexto
    da conversa no banco de dados vetorial, categorizadas por tipo de memória.

    OBRIGATÓRIO: Use esta ferramenta imediatamente se o usuário se apresentar, disser seu nome ou revelar uma preferência nova (ex: 'eu gosto de X', 'trabalho com Y'). Não apenas responda, você deve persistir essa informação.

    Args:
        memories: Lista de objetos Memory contendo o conteúdo e tipo de cada memória.
            Tipos disponíveis:
            - semantic: Conhecimento geral e fatos (ex: "Python é uma linguagem de programação")
            - episodic: Experiências e preferências do usuário (ex: "Usuário prefere café da manhã")
        config: Configuração de execução contendo user_id e thread_id para identificação.

    Returns:
        String confirmando o sucesso do registro ou descrevendo o erro ocorrido.
    """
    print("--- STORE MEMORY TOOL ---")
    
    configurable = config.get("configurable", {})
    user_id = configurable.get("user_id", None)
    thread_id = configurable.get("thread_id", None)

    if not user_id:
        return "Erro: user_id não fornecido na configuração. Memórias não foram armazenadas."

    try:
        list_memories_to_list_documents = []
        for mem in memories:
            list_memories_to_list_documents.append(
                Document(
                    page_content=mem.content,
                    metadata={
                        "memory_type": mem.memory_type.lower(),
                        "user_id": user_id,
                        "thread_id": thread_id
                    }
                )
            )
        vector_store.add_documents(list_memories_to_list_documents)

        return "Memórias armazenadas com sucesso."
    except Exception as e:
        return f"Erro ao armazenar memórias: {str(e)}"
    
@tool
async def retrieve_memories_tool(
        query: Annotated[str, "Consulta necessária para recuperar as memórias mais similares registradas no banco vetorial."],
        memory_type: Annotated[Literal["episodic", "semantic"], "Tipo de memória a ser recuperada"],
        limit: Annotated[int, "Número máximo de memórias a serem recuperadas"],
        config: RunnableConfig
) -> str:
    
    """Recupera memórias de longo prazo do banco vetorial usando busca por similaridade.

    Esta ferramenta busca memórias armazenadas previamente que são semanticamente similares
    à consulta fornecida. É possível filtrar por tipo de memória e limitar a quantidade de resultados.

    ESSENCIAL: Chame esta ferramenta SEMPRE que o usuário perguntar o próprio nome, preferências ou informações pessoais que não foram ditas nesta sessão específica. Esta ferramenta é a única forma de acessar a identidade persistente do usuário no Pinecone.

    Args:
        query: Texto de consulta usado para encontrar memórias semanticamente similares.
        memory_type: Lista de tipos de memória para filtrar os resultados.
            Tipos disponíveis:
            - semantic: Conhecimento geral e fatos
            - episodic: Experiências e preferências do usuário
            Se vazio, busca em todos os tipos.
        limit: Número máximo de memórias a serem retornadas (máximo 10).
        config: Configuração de execução contendo user_id para filtrar memórias do usuário.

    Returns:
        String formatada contendo as memórias encontradas com seus tipos, ou mensagem
        indicando que nenhuma memória relevante foi encontrada.
    """
    print("--- RETRIEVE MEMORIES TOOL ---")

    configurable = config.get("configurable", {})
    user_id = str(configurable.get("user_id"))

    if not user_id:
        return "Erro: user_id não fornecido na configuração. Memórias não podem ser recuperadas."

    try:
      #pinecone_filter = {"user_id": {"$eq": user_id}}
      pinecone_filter = {"user_id": user_id}

      docs = vector_store.similarity_search(query=query, k=limit, filter=pinecone_filter)

      if not docs:
          return "Nenhuma memória encontrada."
      
      results = []
      for doc in docs:
          mem_type = doc.metadata.get("memory_type", "N/A")
          results.append(f"{mem_type}: {doc.page_content}")

      return "\n\n".join(results)
    
    except Exception as e:
        return f"Erro ao recuperar memórias: {str(e)}"


# @tool
# async def search_data_dictionary(
#     query: Annotated[str, "Termos de busca para encontrar tabelas e colunas (ex: 'população', 'sustentabilidade', 'turismo')"],
#     config: RunnableConfig
# ) -> str:
#     """
#     Consulta o manual técnico do banco de dados (Dicionário de Dados).
#     Use esta ferramenta SEMPRE que precisar saber:
#     1. Qual o nome real de uma tabela no banco de dados.
#     2. O significado de colunas específicas (ex: o que é Q01, Q02).
#     3. Quais colunas podem ser usadas para unir (JOIN) duas tabelas.
#     4. Ver uma amostra dos dados para entender o formato (ex: se o estado é 'SC' ou 'Santa Catarina').
#     """
#     print(f"--- CONSULTANDO DICIONÁRIO: {query} ---")
    
#     docs = guide_vector_store.similarity_search(
#         query=query, 
#         k=15, 
#         filter={"type": "dictionary"}, 
#         namespace="data_dictionary"
#     )

#     if not docs:
#         return "Nenhuma tabela ou coluna correspondente encontrada no dicionário."

#     # Formata a resposta para o Agente
#     instrucoes = "RESULTADOS DO DICIONÁRIO DE DADOS:\n"
#     for d in docs:
#         instrucoes += f"\n========================================\n"
#         instrucoes += f"CONTEÚDO: {d.page_content}\n"
    
#     return instrucoes

# @tool
# async def retrieve_dictionary_tool(
#         query: Annotated[str, "Pergunta do usuário para busca semântica no dicionário de dados"],
#         limit: Annotated[int, "Número de trechos do dicionário a recuperar"] = 15,
#         config: RunnableConfig = None,
# ) -> str:
#     """Busca no dicionário de metadados do banco de dados usando similaridade semântica.
 
#     Use esta ferramenta ANTES de qualquer consulta SQL quando a pergunta do usuário
#     envolver dados do banco. Ela retorna quais tabelas e colunas são relevantes para
#     a pergunta, evitando alucinações de nomes técnicos.
 
#     Retorna: trechos do dicionário com nomes exatos de tabelas, colunas e descrições.
#     """
#     print("--- RETRIEVE DICTIONARY TOOL ---")
#     try:
#         docs = guide_vector_store.similarity_search(query=query, k=limit)
#         if not docs:
#             return "Nenhum metadado encontrado no dicionário para esta consulta."
#         results = []
#         for doc in docs:
#             source = doc.metadata.get("source", "dicionário")
#             results.append(f"[{source}]\n{doc.page_content}")
#         return "\n\n---\n\n".join(results)
#     except Exception as e:
#         return f"Erro ao buscar no dicionário: {str(e)}"
 


toolkit = SQLDatabaseToolkit(db=db_bussola, llm=model)

db_tools = toolkit.get_tools()
# excluded_tool_names = ["sql_db_query_checker"]
# db_tools_filtered = [
#     tool for tool in db_tools 
#     if tool.name not in excluded_tool_names
# ]
tools_agent = [store_memory_tool, retrieve_memories_tool] + db_tools
tool_node = ToolNode(tools=tools_agent)