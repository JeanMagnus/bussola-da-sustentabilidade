from email.mime import text
import json
import re
from sqlalchemy import inspect
import unicodedata
from app.agent.state import AgentState
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langgraph.prebuilt import ToolNode, InjectedState
from langchain_core.runnables import RunnableConfig
from langchain_core.documents import Document
from langchain_core.tools import tool
from typing import Annotated, List, Literal, Optional
from app.core.config import model, db_bussola
from app.agent.memory import vector_store, Memory, guide_vector_store, about_vector_store

TABLE_ALIASES: dict[str, str] = {
    "salarios_e_visitas": "salarios_e_visitas",
    "salários_e_visitas": "salarios_e_visitas",
    "salarios": "salarios_e_visitas",
    "visitas": "salarios_e_visitas",
    "emprego": "salarios_e_visitas",
    "situacional": "situacional_2023",
    "situacional_2023": "situacional_2023",
    "situacional2023": "situacional_2023",
    "ibge": "ibge",
    "municipios": "ibge",
    "municípios": "ibge",
    "cidades": "ibge",
    "selo": "selo",
    "certificacao": "selo",
    "certificação": "selo",
}

CERTIFIED_CITIES = [
    "Arroio Trinta", "Bombinhas", "Bom Jardim da Serra", "Frei Rogério",
    "Itá", "Navegantes", "Orleans", "São Joaquim", "Treze Tílias", "Urubici",
    "Apodi", "São Miguel do Gostoso", "Tibau do Sul", "Fernando de Noronha",
]

TEXT_COLUMNS = {
    "cidade", "municipio", "município", "destino", "nome",
    "regiao", "região", "mesorregiao", "mesorregião",
    "microrregiao", "microrregião", "regiao_intermediaria",
    "regiao_turistíca", "regiao_turistica", "estado", "uf",
}

BOOL_MAP = {
    "sim": "Sim", "s": "Sim", "yes": "Sim", "true": "Sim", "1": "Sim",
    "não": "Não", "nao": "Não", "no": "Não", "false": "Não", "0": "Não",
}

def _strip_accents(text: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", text)
        if unicodedata.category(c) != "Mn"
    )

def _normalize_table(name: str) -> str:
    clean = name.strip().lower()
    clean_no_accent = _strip_accents(clean)
    return TABLE_ALIASES.get(clean, TABLE_ALIASES.get(clean_no_accent, clean))

def _closest_city(raw: str) -> Optional[str]:
    raw_norm = _strip_accents(raw.strip().lower())
    for city in CERTIFIED_CITIES:
        if raw_norm in _strip_accents(city.lower()) or _strip_accents(city.lower()) in raw_norm:
            return city
    return None

def _build_text_filter(column: str, value: str) -> str:
    safe_value = value.replace("'", "''")
    return f"unaccent({column}::text) ILIKE unaccent('%{safe_value}%')"

def _build_numeric_filter(column: str, raw_value: str, operator: str = "=") -> str:
    cleaned = raw_value.strip()
    if re.match(r"^\d{1,3}(\.\d{3})*(,\d+)?$", cleaned):
        cleaned = cleaned.replace(".", "").replace(",", ".")
    elif re.match(r"^\d{1,3}(,\d{3})*(\.\d+)?$", cleaned):
        cleaned = cleaned.replace(",", "")
    cleaned = re.sub(r"[^\d.\-]", "", cleaned)
    return f"CAST(REPLACE({column}::text, ',', '.') AS NUMERIC) {operator} {cleaned}"

def _build_avg_expression(column: str) -> str:
    return f"AVG(CAST(REPLACE({column}::text, ',', '.') AS NUMERIC))"

def _build_date_filter(column: str, value: str) -> str:
    v = value.strip()
    if re.match(r"^\d{2}/\d{2}/\d{4}$", v):
        d, m, y = v.split("/")
        v = f"{y}-{m}-{d}"
    return f"DATE({column}) = '{v}'::DATE"

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
def sql_query_builder(
    table: Annotated[str, "Nome da tabela principal. Aliases: 'situacional', 'ibge', 'salarios', etc."],
    columns: Annotated[list[str], "Colunas a selecionar. NUNCA use ['*']."],
    filters: Annotated[list[dict], "Lista de dicts: {'column', 'value', 'type', 'operator', 'logic'}"] = [],
    joins: Annotated[list[dict], "JOINs: {'type', 'table', 'on'}"] = [],
    aggregation: Annotated[Optional[Literal["avg", "count", "sum", "min", "max", "none"]], "Agregação SQL"] = None,
    group_by: Annotated[Optional[str], "Colunas GROUP BY separadas por vírgula."] = None,
    order_by: Annotated[Optional[str], "Cláusula ORDER BY sem a palavra-chave."] = None,
    limit: Annotated[int, "Máximo de linhas (reforçado para 15)."] = 10,
) -> str:
    """
    Gera uma query SQL SELECT pronta para execução via sql_db_query.
    Aplica automaticamente unaccent, ILIKE, CAST de valores BR e resolução de aliases.
    """
    resolved_table = _normalize_table(table)
    safe_limit = min(max(1, limit), 15)

    if not columns or columns == ["*"]:
        return "ERRO: Especifique as colunas. Não use ['*']."

    agg = (aggregation or "none").lower()
    select_parts: list[str] = []

    for col in columns:
        col_clean = col.strip()
        if agg == "avg": select_parts.append(f"{_build_avg_expression(col_clean)} AS media_{col_clean}")
        elif agg == "count": 
            select_parts.append("COUNT(*) AS total")
            break
        elif agg == "sum": select_parts.append(f"SUM(CAST(REPLACE({col_clean}::text, ',', '.') AS NUMERIC)) AS soma_{col_clean}")
        elif agg in ["min", "max"]: select_parts.append(f"{agg.upper()}(CAST(REPLACE({col_clean}::text, ',', '.') AS NUMERIC)) AS {agg}_{col_clean}")
        else: select_parts.append(col_clean)

    if group_by and agg != "none":
        for gb_col in [c.strip() for c in group_by.split(",")]:
            if gb_col and gb_col not in [col.strip() for col in columns]:
                select_parts.insert(0, gb_col)

    select_clause = "SELECT " + ", ".join(select_parts)
    from_clause = f"FROM {resolved_table}"
    
    join_parts = [f"{j.get('type', 'INNER').upper()} JOIN {_normalize_table(j.get('table', ''))} ON {j.get('on', '')}" for j in joins if j.get('table') and j.get('on')]

    where_conditions, pending_logic = [], "AND"
    for flt in filters:
        col, val = flt.get("column", "").strip(), str(flt.get("value", "")).strip()
        ftype, operator, logic = flt.get("type", "auto").lower(), flt.get("operator", "=").upper(), flt.get("logic", "AND").upper()
        if not col or not val: continue

        if ftype == "auto":
            if col.lower() in TEXT_COLUMNS or re.search(r"[a-zA-ZÀ-ú]{3,}", val): ftype = "text"
            elif re.match(r"^\d{2}/\d{2}/\d{4}$", val): ftype = "date"
            elif val.lower() in BOOL_MAP: ftype = "bool"
            elif re.search(r"\d", val): ftype = "numeric"
            else: ftype = "text"

        if ftype == "text":
            if col.lower() in ("cidade", "municipio", "município", "destino"):
                suggestion = _closest_city(val)
                if suggestion: val = suggestion
            condition = _build_text_filter(col, val)
        elif ftype == "numeric":
            condition = f"CAST(REPLACE({col}::text, ',', '.') AS NUMERIC) BETWEEN {val}" if operator == "BETWEEN" else _build_numeric_filter(col, val, operator)
        elif ftype == "date": condition = _build_date_filter(col, val)
        elif ftype == "bool":
            safe_val = BOOL_MAP.get(val.lower(), val).replace("'", "''")
            condition = f"unaccent({col}::text) ILIKE unaccent('{safe_val}')"
        else: condition = _build_text_filter(col, val)

        where_conditions.append(f"{pending_logic} {condition}" if where_conditions else condition)
        pending_logic = logic

    where_clause = ("WHERE " + " ".join(where_conditions)) if where_conditions else ""
    query = "\n".join(p for p in [select_clause, from_clause, *join_parts, where_clause, f"GROUP BY {group_by}" if group_by else "", f"ORDER BY {order_by}" if order_by else "", f"LIMIT {safe_limit}"] if p)
    
    print(f"\n[SQL_QUERY_BUILDER] Query:\n{query}\n")
    return query

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
    - NÃO gere tags `<|DSML|>`.
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

        # MAX_CHARS = 10000

        resultado_str = str(resultado_bruto)

        # if len(resultado_str) > MAX_CHARS:
        #     print(
        #         f"   [Aviso] Resultado longo ({len(resultado_str)} chars). "
        #         f"Truncando para {MAX_CHARS}."
        #     )
        #     return (
        #         resultado_str[:MAX_CHARS]
        #         + '... [RESULTADO CORTADO PARA POUPAR TOKENS. '
        #         + 'REFAÇA A QUERY COM UM "LIMIT" MENOR OU AGREGAÇÃO SE PRECISAR DE MAIS DADOS].'
        #     )
        
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
        
        tables = [t.strip() for t in table_names.split(",") if t.strip()]
        
        if not tables:
            return "ERRO: Nenhuma tabela foi fornecida. Envie os nomes separados por vírgula."

        inspector = inspect(db_bussola._engine)
        schema_info = []
        
        for table in tables:
            try:
                columns = inspector.get_columns(table)
                pk_cols = inspector.get_pk_constraint(table).get('constrained_columns', [])
                
                col_details = []
                for c in columns:
                    pk_marker = "*" if c['name'] in pk_cols else ""
                    col_details.append(f"{c['name']}{pk_marker} ({c['type']})")
                
                schema_info.append(f"Tabela '{table}': {', '.join(col_details)}")
                
            except Exception as e:
                schema_info.append(f"Tabela '{table}': Erro - Esta tabela não existe no banco de dados.")
        
        resultado_str = "\n".join(schema_info)
        
        # MAX_CHARS = 1000 
        # if len(resultado_str) > MAX_CHARS:
        #     print(f"   [Aviso] Schema muito longo ({len(resultado_str)} chars). Truncando para {MAX_CHARS}.")
        #     return resultado_str[:MAX_CHARS] + '... [SCHEMA CORTADO PARA POUPAR TOKENS].'

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



toolkit = SQLDatabaseToolkit(db=db_bussola, llm=model)

db_tools = toolkit.get_tools()
# , "sql_db_schema", "sql_db_list_tables"
excluded_tool_names = ["sql_db_query_checker" , "sql_db_schema", "sql_db_list_tables"]   # Exclui ferramentas de consulta direta para forçar o uso do dicionário
db_tools_filtered = [
    tool for tool in db_tools 
    if tool.name not in excluded_tool_names
]
#tools_agent = [store_memory_tool, retrieve_memories_tool, retrieve_last_ai_message_tool, retrieve_about] + db_tools
tools_agent = [store_memory_tool, retrieve_memories_tool, retrieve_last_ai_message_tool, sql_db_query, retrieve_about, sql_db_schema]
tools_chat = [store_memory_tool, retrieve_memories_tool, retrieve_last_ai_message_tool, retrieve_about]
tools_rag = [retrieve_last_ai_message_tool]
tool_node = ToolNode(tools=tools_agent)