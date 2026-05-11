from email.mime import text
import json
import re
from sqlalchemy import inspect
from app.agent.state import AgentState
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langgraph.prebuilt import ToolNode, InjectedState
from langchain_core.runnables import RunnableConfig
from langchain_core.documents import Document
from langchain_core.tools import tool
from typing import Annotated, List, Literal
from app.core.config import model, db_bussola
from app.agent.memory import vector_store, Memory, guide_vector_store, about_vector_store


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


@tool
async def retrieve_last_ai_message_tool(state: Annotated[AgentState, InjectedState], config: RunnableConfig) -> str:
    """Recupera a última mensagem gerada pela IA na conversa atual.

    Esta ferramenta é útil para acessar o conteúdo da última resposta da IA, seja para referência
    em mensagens futuras ou para depuração. Ela retorna apenas o texto da última mensagem da IA.

    Utilize essa ferramenta em caso de necessidade de referenciar ou reutilizar a última resposta da IA, ou para verificar o que foi dito antes de tomar uma ação baseada nessa resposta.
    Quando o usuário informar que não entendeu ou pedir para repetir algo, esta ferramenta pode ser usada para recuperar a última mensagem da IA e reformulá-la ou explicá-la de maneira diferente.
    Quando precisar conectar dados de respostas anteriores da IA com ações ou decisões atuais, esta ferramenta pode fornecer o contexto necessário.

    Args:
        state: O estado atual do agente, contendo o histórico de mensagens e outras informações relevantes.
        config: Configuração de execução (não utilizada nesta ferramenta, mas incluída para consistência).

    Returns:
        String contendo o texto da última mensagem gerada pela IA, ou uma mensagem indicando que não há mensagens disponíveis.
    """
    print("--- RETRIEVE LAST AI MESSAGE TOOL ---")
    
    try:
        last_ai_message = state.get("last_msg_ai", None)
        if last_ai_message:
            return f"A última mensagem que você enviou foi: {last_ai_message}"
        else:
            return "Nenhuma mensagem da IA encontrada no estado atual."
    except Exception as e:
        return f"Erro ao recuperar a última mensagem da IA: {str(e)}"

@tool
def sql_db_query(
    query: Annotated[
        str,
        """
        Consulta SQL SELECT a ser executada no banco PostgreSQL.

        REGRAS OBRIGATÓRIAS:
        - Use apenas SELECT.
        - É obrigatório usar LIMIT, no máximo LIMIT 15.
        - Nunca use SELECT *.
        - Para filtros textuais com nomes de cidades, municípios, destinos ou nomes próprios,
          SEMPRE use busca tolerante a acentos e maiúsculas/minúsculas.

        PADRÃO OBRIGATÓRIO PARA CIDADES/NOMES:
        Use:
            unaccent(coluna::text) ILIKE unaccent('%valor%')

        Exemplo correto:
            SELECT cidade, uf, codigo_municipio
            FROM situacional_2023
            WHERE unaccent(cidade::text) ILIKE unaccent('%Treze Tilias%')
            LIMIT 15

        Exemplo errado:
            WHERE cidade ILIKE '%Treze Tilias%'

        Exemplo errado:
            WHERE cidade = 'Treze Tilias'
        """
    ]
) -> str:
    """
    A ÚNICA ferramenta disponível para acessar o banco de dados.

    Executa consultas SQL SELECT no PostgreSQL e retorna os resultados.

    INSTRUÇÕES CRÍTICAS PARA O AGENTE:
    - Você JÁ POSSUI o schema no prompt.
    - NÃO invoque ferramentas como `sql_db_list_tables` ou `sql_db_schema`.
    - NÃO gere tags `<|DSML|>`.
    - NÃO use SELECT *.
    - Para nomes de cidades, municípios, destinos ou nomes próprios, use obrigatoriamente:

        unaccent(coluna::text) ILIKE unaccent('%valor%')

    Isso evita erro com:
    - acentos: "Tílias" vs "Tilias";
    - maiúsculas/minúsculas: "Bombinhas" vs "BOMBINHAS";
    - variações simples de escrita.
    """

    query = query.strip()
    query_upper = query.upper()

    forbidden_keywords = [
        "DROP ",
        "DELETE ",
        "UPDATE ",
        "INSERT ",
        "ALTER ",
        "TRUNCATE ",
        "GRANT ",
        "REVOKE ",
        "CREATE ",
        "REPLACE ",
    ]

    if any(keyword in query_upper for keyword in forbidden_keywords):
        return "ERRO DE SEGURANÇA: Apenas consultas SELECT são permitidas."

    if not query_upper.startswith("SELECT"):
        return "ERRO DE SEGURANÇA: A consulta deve começar com SELECT."

    if "SELECT *" in query_upper:
        return (
            "ERRO DE CONSULTA: Não use SELECT *. "
            "Selecione apenas as colunas necessárias para responder ao usuário."
        )

    if " LIMIT " not in query_upper:
        return (
            "ERRO DE CONSULTA: Toda consulta precisa usar LIMIT, no máximo LIMIT 15."
        )

    limit_match = re.search(r"\bLIMIT\s+(\d+)\b", query_upper)
    if limit_match:
        limit_value = int(limit_match.group(1))
        if limit_value > 15:
            return (
                "ERRO DE CONSULTA: O LIMIT máximo permitido é 15. "
                "Refaça a query usando LIMIT 15 ou menor."
            )

    text_columns = [
        "cidade",
        "municipio",
        "município",
        "destino",
        "nome",
    ]

    uses_text_column = any(
        re.search(rf"\b{col}\b", query, flags=re.IGNORECASE)
        for col in text_columns
    )

    uses_text_filter = bool(
        re.search(
            r"\b(ILIKE|LIKE|=|IN)\s*(\(|')",
            query,
            flags=re.IGNORECASE,
        )
    )

    uses_unaccent = "unaccent(" in query.lower()

    if uses_text_column and uses_text_filter and not uses_unaccent:
        return (
            "ERRO DE CONSULTA: Para filtros textuais com cidade, município, destino "
            "ou nome próprio, use busca tolerante a acentos e maiúsculas/minúsculas.\n\n"
            "Use este padrão:\n"
            "unaccent(coluna::text) ILIKE unaccent('%valor%')\n\n"
            "Exemplo:\n"
            "SELECT cidade, uf, codigo_municipio\n"
            "FROM situacional_2023\n"
            "WHERE unaccent(cidade::text) ILIKE unaccent('%Treze Tilias%')\n"
            "LIMIT 15;"
        )

    try:
        print(f"\n [TOOL SQL] Executando: {query}")

        resultado_bruto = db_bussola.run(query)

        if not resultado_bruto or str(resultado_bruto).strip() == "":
            return "A consulta foi executada com sucesso, mas retornou 0 resultados."

        MAX_CHARS = 10000

        resultado_str = str(resultado_bruto)

        if len(resultado_str) > MAX_CHARS:
            print(
                f"   [Aviso] Resultado longo ({len(resultado_str)} chars). "
                f"Truncando para {MAX_CHARS}."
            )
            return (
                resultado_str[:MAX_CHARS]
                + '... [RESULTADO CORTADO PARA POUPAR TOKENS. '
                + 'REFAÇA A QUERY COM UM "LIMIT" MENOR OU AGREGAÇÃO SE PRECISAR DE MAIS DADOS].'
            )
        
        resultado_bruto = db_bussola.run(query)

        print(f"   [TOOL SQL] Resultado bruto repr: {repr(resultado_bruto)[:1000]}")

        if not resultado_bruto or str(resultado_bruto).strip() == "":
            print("   [TOOL SQL] Resultado vazio.")
            return "A consulta foi executada com sucesso, mas retornou 0 resultados."

        return resultado_str

    except Exception as e:
        erro_limpo = str(e).split("\n")[0]
        print(f"   [Erro DB] {erro_limpo}")

        if "unaccent" in erro_limpo.lower():
            return (
                "Erro de execução SQL: a função unaccent parece não estar habilitada "
                "no banco de dados. É necessário habilitar a extensão PostgreSQL "
                "unaccent com: CREATE EXTENSION IF NOT EXISTS unaccent;"
            )

        return (
            f"Erro de Sintaxe ou Execução SQL: {erro_limpo}. "
            "Revise a query, os nomes das colunas e os tipos utilizados."
        )


@tool
def sql_db_schema(
    table_names: Annotated[str, "Uma string com os nomes das tabelas separados por vírgula (ex: 'ibge, selo')."]
) -> str:
    """
    Retorna a estrutura OTIMIZADA (apenas colunas, tipos e chaves primárias) das tabelas solicitadas.
    Use esta ferramenta IMEDIATAMENTE se receber um erro de "column does not exist" ou 
    "relation does not exist" para descobrir os nomes exatos antes de tentar a query novamente.
    """
    try:
        print(f"\n [TOOL SCHEMA] Inspecionando tabelas: {table_names}")
        
        # Limpa e separa os nomes das tabelas enviados pelo LLM
        tables = [t.strip() for t in table_names.split(",") if t.strip()]
        
        if not tables:
            return "ERRO: Nenhuma tabela foi fornecida. Envie os nomes separados por vírgula."

        # Extrai o "motor" do SQLAlchemy por trás do LangChain para inspecionar diretamente
        inspector = inspect(db_bussola._engine)
        schema_info = []
        
        for table in tables:
            try:
                # Busca as colunas e a chave primária
                columns = inspector.get_columns(table)
                pk_cols = inspector.get_pk_constraint(table).get('constrained_columns', [])
                
                col_details = []
                for c in columns:
                    # Adiciona um asterisco (*) para sinalizar que é Primary Key
                    pk_marker = "*" if c['name'] in pk_cols else ""
                    # Ex: id* (INTEGER) ou nome (VARCHAR)
                    col_details.append(f"{c['name']}{pk_marker} ({c['type']})")
                
                # Formatação ultracompacta
                schema_info.append(f"Tabela '{table}': {', '.join(col_details)}")
                
            except Exception as e:
                # Se o LLM inventar um nome de tabela que não existe
                schema_info.append(f"Tabela '{table}': Erro - Esta tabela não existe no banco de dados.")
        
        resultado_str = "\n".join(schema_info)
        
        # Proteção contra tabelas monstruosas (ex: tabelas com 200 colunas)
        MAX_CHARS = 1000 
        if len(resultado_str) > MAX_CHARS:
            print(f"   [Aviso] Schema muito longo ({len(resultado_str)} chars). Truncando para {MAX_CHARS}.")
            return resultado_str[:MAX_CHARS] + '... [SCHEMA CORTADO PARA POUPAR TOKENS].'

        return resultado_str

    except Exception as e:
        erro_limpo = str(e).split('\n')[0] 
        print(f"   [Erro Schema] {erro_limpo}")
        return f"Erro ao tentar ler a estrutura do banco: {erro_limpo}"

@tool
def retrieve_about(
    query: Annotated[str, "Consulta para recuperar informações sobre a organização, missão, equipe ou outras informações relevantes."],
    limit: Annotated[int, "Número máximo de trechos institucionais a serem recuperados"]
) -> str:
    """
    Consulta o índice 'about' para recuperar informações sobre a organização, missão, equipe ou outras informações relevantes.
    Use esta ferramenta SEMPRE que o usuário fizer perguntas sobre a própria organização, seus objetivos, equipe ou informações institucionais.
    Esta ferramenta é a única forma de acessar o conhecimento sobre a organização persistente no Pinecone.
    """
    print(f"--- CONSULTANDO ÍNDICE 'ABOUT' ---")
    
    try:
        docs = about_vector_store.similarity_search(
            query=query, 
            k=limit, 
            filter={"type": "institutional_info"}, 
            namespace="about"
        )

        if not docs:
            return "Nenhuma informação relevante encontrada."

        instrucoes = "RESULTADOS:\n"
        for d in docs:
            instrucoes += f"\n========================================\n"
            instrucoes += f"CONTEÚDO: {d.page_content}\n"
        
        return instrucoes
    
    except Exception as e:
        return f"Erro ao buscar no índice 'about': {str(e)}"

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
# , "sql_db_schema", "sql_db_list_tables"
excluded_tool_names = ["sql_db_query_checker" , "sql_db_schema", "sql_db_list_tables"]   # Exclui ferramentas de consulta direta para forçar o uso do dicionário
db_tools_filtered = [
    tool for tool in db_tools 
    if tool.name not in excluded_tool_names
]
tools_agent = [store_memory_tool, retrieve_memories_tool, retrieve_last_ai_message_tool, retrieve_about, sql_db_query, sql_db_schema]
tools_chat = [store_memory_tool, retrieve_memories_tool, retrieve_last_ai_message_tool, retrieve_about]
tools_rag = [retrieve_last_ai_message_tool]
tool_node = ToolNode(tools=tools_agent)