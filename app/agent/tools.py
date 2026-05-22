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
from pydantic import BaseModel, Field
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
    query: Annotated[str, "Query SELECT para executar no PostgreSQL. LIMIT obrigatório (máx 15)."]
) -> str:
    """Executa SELECT no banco. Use sql_query_builder para montar a query antes."""

    query = query.strip()
    query_upper = query.upper()

    FORBIDDEN = ["DROP ", "DELETE ", "UPDATE ", "INSERT ",
                 "ALTER ", "TRUNCATE ", "GRANT ", "REVOKE ", "CREATE "]

    if any(kw in query_upper for kw in FORBIDDEN):
        return "ERRO DE SEGURANÇA: Apenas SELECT é permitido."
    if not query_upper.startswith("SELECT"):
        return "ERRO: A consulta deve começar com SELECT."
    if "SELECT *" in query_upper:
        return "ERRO: Não use SELECT *. Especifique as colunas necessárias."
    if " LIMIT " not in query_upper:
        return "ERRO: Toda query precisa de LIMIT (máximo 15)."

    limit_match = re.search(r"\bLIMIT\s+(\d+)\b", query_upper)
    if limit_match and int(limit_match.group(1)) > 15:
        return "ERRO: LIMIT máximo é 15."

    # Checagem de unaccent para colunas textuais
    uses_text_col = any(
        re.search(rf"\b{col}\b", query, flags=re.IGNORECASE)
        for col in ["cidade", "municipio", "município", "destino", "nome"]
    )
    uses_filter = bool(re.search(r"\b(ILIKE|LIKE|=|IN)\s*(\(|')", query, re.IGNORECASE))

    if uses_text_col and uses_filter and "unaccent(" not in query.lower():
        return (
            "ERRO: Use unaccent para filtros textuais:\n"
            "  unaccent(coluna::text) ILIKE unaccent('%valor%')"
        )

    try:
        print(f"[SQL] Executando: {query}")
        resultado = db_bussola.run(query)  # ← executa UMA vez

        if not resultado or str(resultado).strip() == "":
            return "Query executada com sucesso, mas sem resultados."

        return str(resultado)

    except Exception as e:
        erro = str(e).split("\n")[0]
        print(f"[SQL ERROR] {erro}")

        if "unaccent" in erro.lower():
            return "Erro: extensão unaccent não habilitada. Execute: CREATE EXTENSION IF NOT EXISTS unaccent;"
        if "does not exist" in erro.lower():
            return f"Erro: coluna ou tabela não existe. Use sql_db_schema para verificar. Detalhe: {erro}"

        return f"Erro SQL: {erro}"



@tool
def sql_db_schema(
    table_names: Annotated[str, "Nomes das tabelas separados por vírgula"]
) -> str:
    """Retorna estrutura das tabelas. Use ao receber erro 'column does not exist'."""
    try:
        tables = [_normalize_table(t) for t in table_names.split(",") if t.strip()]  # ← fix

        if not tables:
            return "ERRO: Nenhuma tabela fornecida."

        inspector = inspect(db_bussola._engine)
        schema_info = []

        for table in tables:
            try:
                columns = inspector.get_columns(table)
                pk_cols = inspector.get_pk_constraint(table).get("constrained_columns", [])
                col_details = [
                    f"{c['name']}{'*' if c['name'] in pk_cols else ''} ({c['type']})"
                    for c in columns
                ]
                schema_info.append(f"Tabela '{table}': {', '.join(col_details)}")
            except Exception:
                schema_info.append(f"Tabela '{table}': não existe no banco.")

        return "\n".join(schema_info)

    except Exception as e:
        return f"Erro ao ler estrutura: {str(e).split(chr(10))[0]}"

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


class SQLStrategyInput(BaseModel):
    task_type: Literal[
        "lookup_cidades",
        "comparacao_cidades",
        "resumo_avaliacoes",
        "ranking_notas",
        "evolucao_temporal",
        "detalhamento_criterios",
        "geral"
    ] = Field(
        description="Tipo da tarefa SQL identificada."
    )

    user_question: str = Field(
        description="Pergunta original ou resolvida do usuário."
    )

    entities: Optional[list[str]] = Field(
        default=None,
        description="Entidades relevantes, como ['Apodi-RN', 'Bombinhas-SC']."
    )


@tool(args_schema=SQLStrategyInput)
def get_sql_strategy(
    task_type: str,
    user_question: str,
    entities: Optional[list[str]] = None,
) -> str:
    """
    Retorna uma estratégia SQL recomendada para gerar uma única consulta mais objetiva.
    Use antes de sql_db_query quando a pergunta exigir consulta ao banco.
    """

    strategies = {
        "lookup_cidades": """
ESTRATÉGIA SQL: LOOKUP DE CIDADES

Use quando o usuário pedir:
- código IBGE;
- região;
- mesorregião;
- microrregião;
- população;
- PIB;
- IDH;
- bioma;
- dados territoriais de cidades específicas.

FORMATO:
- Use uma única query.
- Use CTE cidades_alvo(cidade_ref, uf_ref) com VALUES.
- Use LEFT JOIN com ibge.
- Retorne uma linha por cidade solicitada.
- Preserve cidade e UF.
- Não use ILIKE quando cidade e UF estiverem disponíveis.
- Não use LIMIT se a lista fechada já estiver na CTE.

MODELO:

WITH cidades_alvo(cidade_ref, uf_ref) AS (
    VALUES
        ('Cidade1', 'UF'),
        ('Cidade2', 'UF')
)
SELECT
    ca.cidade_ref AS cidade_solicitada,
    ca.uf_ref AS uf_solicitada,
    i.codigo_municipio,
    i.regiao_intermediaria,
    i.mesorregiao,
    i.microrregiao,
    i.populacao,
    i.pib,
    i.idhm,
    i.bioma
FROM cidades_alvo ca
LEFT JOIN ibge i
    ON unaccent(upper(i.cidade::text)) = unaccent(upper(ca.cidade_ref))
   AND upper(i.estado::text) = upper(ca.uf_ref)
ORDER BY ca.uf_ref, ca.cidade_ref;

RESULTADO SUFICIENTE:
- Uma linha por cidade solicitada, mesmo que alguns campos venham nulos.
- Se retornar as cidades solicitadas com as colunas pedidas, não consulte novamente.
""",

        "comparacao_cidades": """
ESTRATÉGIA SQL: COMPARAÇÃO DE CIDADES

Use quando o usuário pedir:
- comparar cidades;
- diferenças entre destinos;
- qual cidade tem melhor desempenho;
- comparação territorial, socioeconômica ou de notas.

FORMATO:
- Use uma única query consolidada.
- Use CTE cidades_alvo.
- Crie CTEs para dados territoriais, selo e métricas de notas.
- Retorne preferencialmente uma linha por cidade.
- Não faça uma query separada para cada cidade.

MODELO:

WITH cidades_alvo(cidade_ref, uf_ref) AS (
    VALUES
        ('Cidade1', 'UF'),
        ('Cidade2', 'UF')
),
dados_ibge AS (
    SELECT
        ca.cidade_ref,
        ca.uf_ref,
        i.codigo_municipio,
        i.regiao_intermediaria,
        i.mesorregiao,
        i.microrregiao,
        i.populacao,
        i.pib,
        i.idhm,
        i.salario_medio,
        i.area_territorial,
        i.bioma,
        i.sistema_costeiro
    FROM cidades_alvo ca
    LEFT JOIN ibge i
        ON unaccent(upper(i.cidade::text)) = unaccent(upper(ca.cidade_ref))
       AND upper(i.estado::text) = upper(ca.uf_ref)
),
selo_gd AS (
    SELECT
        ca.cidade_ref,
        ca.uf_ref,
        s.selo
    FROM cidades_alvo ca
    LEFT JOIN selo s
        ON upper(s.chave) = upper(ca.cidade_ref || '-' || ca.uf_ref)
),
notas AS (
    SELECT
        ca.cidade_ref,
        ca.uf_ref,
        AVG(CAST(REPLACE(t.nota, ',', '.') AS NUMERIC)) AS media_top100_30,
        COUNT(t.nota) AS qtd_criterios_top100_30,
        MAX(CAST(REPLACE(t.nota, ',', '.') AS NUMERIC)) AS melhor_nota_top100_30,
        MIN(CAST(REPLACE(t.nota, ',', '.') AS NUMERIC)) AS pior_nota_top100_30
    FROM cidades_alvo ca
    LEFT JOIN top100_30 t
        ON unaccent(upper(t.cidade::text)) = unaccent(upper(ca.cidade_ref))
       AND upper(t.estado::text) = upper(ca.uf_ref)
       AND t.nota IS NOT NULL
    GROUP BY ca.cidade_ref, ca.uf_ref
)
SELECT
    d.cidade_ref AS cidade,
    d.uf_ref AS uf,
    d.codigo_municipio,
    d.regiao_intermediaria,
    d.mesorregiao,
    d.microrregiao,
    d.populacao,
    d.pib,
    d.idhm,
    d.salario_medio,
    d.area_territorial,
    d.bioma,
    d.sistema_costeiro,
    s.selo,
    n.media_top100_30,
    n.qtd_criterios_top100_30,
    n.melhor_nota_top100_30,
    n.pior_nota_top100_30
FROM dados_ibge d
LEFT JOIN selo_gd s
    ON d.cidade_ref = s.cidade_ref
   AND d.uf_ref = s.uf_ref
LEFT JOIN notas n
    ON d.cidade_ref = n.cidade_ref
   AND d.uf_ref = n.uf_ref
ORDER BY d.cidade_ref;

RESULTADO SUFICIENTE:
- Uma linha por cidade comparada.
- Se houver dados territoriais e pelo menos alguma métrica ou status disponível, responda.
- Não consulte top100_15 automaticamente se top100_30 já trouxe dados úteis.
""",

        "resumo_avaliacoes": """
ESTRATÉGIA SQL: RESUMO DE AVALIAÇÕES

Use quando o usuário perguntar:
- quais avaliações uma cidade possui;
- quais dados de avaliação existem;
- quais foram as avaliações de uma cidade;
- disponibilidade de Top100, GD ou pesquisa situacional.

FORMATO:
- Não busque todos os detalhes de primeira.
- Faça primeiro um resumo por tipo de avaliação.
- Retorne uma linha por tipo de avaliação.
- Use UNION ALL para consolidar Top100 30, Top100 15 e pesquisa situacional.

MODELO:

WITH cidade_alvo AS (
    SELECT codigo_municipio, cidade, estado
    FROM ibge
    WHERE unaccent(upper(cidade::text)) = unaccent(upper('Cidade'))
      AND upper(estado::text) = upper('UF')
    LIMIT 1
),
avaliacoes AS (
    SELECT
        'Top 100 (30 critérios)' AS tipo_avaliacao,
        COUNT(*) AS qtd_registros,
        AVG(CAST(REPLACE(nota, ',', '.') AS NUMERIC)) AS media_nota
    FROM top100_30
    WHERE unaccent(upper(cidade::text)) = unaccent(upper('Cidade'))
      AND upper(estado::text) = upper('UF')
      AND nota IS NOT NULL

    UNION ALL

    SELECT
        'Top 100 (15 critérios)' AS tipo_avaliacao,
        COUNT(*) AS qtd_registros,
        AVG(CAST(REPLACE(nota, ',', '.') AS NUMERIC)) AS media_nota
    FROM top100_15
    WHERE unaccent(upper(cidade::text)) = unaccent(upper('Cidade'))
      AND upper(estado::text) = upper('UF')
      AND nota IS NOT NULL

    UNION ALL

    SELECT
        'Pesquisa Situacional' AS tipo_avaliacao,
        COUNT(*) AS qtd_registros,
        AVG(nota::numeric) AS media_nota
    FROM situacional_2023_pivot_median s
    JOIN cidade_alvo c
      ON s.codigo_municipio = c.codigo_municipio
    WHERE s.nota IS NOT NULL
)
SELECT *
FROM avaliacoes
WHERE qtd_registros > 0
ORDER BY tipo_avaliacao;

RESULTADO SUFICIENTE:
- Uma linha por tipo de avaliação encontrada.
- Se o usuário pediu apenas "quais avaliações", não busque detalhes de critérios/perguntas ainda.
- Só busque detalhes se o usuário pedir explicitamente.
""",

        "ranking_notas": """
ESTRATÉGIA SQL: RANKING POR NOTAS

Use quando o usuário perguntar:
- melhores notas;
- piores notas;
- ranking;
- cidades com melhor desempenho em um tema ou critério.

FORMATO:
- Use uma única query.
- Se houver termo temático, primeiro encontre critérios relevantes em criterios.
- Cruze os critérios encontrados com top100_30.
- Calcule média ou nota conforme a pergunta.
- Ordene e limite o resultado.

MODELO:

WITH criterios_alvo AS (
    SELECT criterio
    FROM criterios
    WHERE unaccent(criteria_name_pt::text) ILIKE unaccent('%termo%')
       OR unaccent(criteria_description_pt::text) ILIKE unaccent('%termo%')
       OR unaccent(topic_description_pt::text) ILIKE unaccent('%termo%')
),
ranking AS (
    SELECT
        t.cidade,
        t.estado,
        AVG(CAST(REPLACE(t.nota, ',', '.') AS NUMERIC)) AS media_nota,
        COUNT(*) AS qtd_criterios
    FROM top100_30 t
    JOIN criterios_alvo c
      ON t.criterio = c.criterio
    WHERE t.nota IS NOT NULL
    GROUP BY t.cidade, t.estado
)
SELECT *
FROM ranking
ORDER BY media_nota DESC
LIMIT 20;

RESULTADO SUFICIENTE:
- Pelo menos algumas cidades ranqueadas com métrica calculada.
- Não faça nova busca se o ranking já responde à pergunta.
""",

        "evolucao_temporal": """
ESTRATÉGIA SQL: EVOLUÇÃO TEMPORAL

Use quando o usuário perguntar:
- evolução;
- histórico;
- ao longo dos anos;
- ciclos;
- aproveitamento.

FORMATO:
- Use uma query agregada por ano.
- Retorne uma linha por cidade e ano.
- Use timeline_gd quando o foco for histórico/ciclos/aproveitamento.

MODELO:

WITH cidades_alvo(cidade_ref, uf_ref) AS (
    VALUES
        ('Cidade', 'UF')
)
SELECT
    ca.cidade_ref AS cidade,
    ca.uf_ref AS uf,
    t.ano,
    t.origem,
    t.total,
    t.numero_criterios,
    t.aproveitamento
FROM cidades_alvo ca
LEFT JOIN timeline_gd t
    ON upper(t.chave) = upper(ca.cidade_ref || '-' || ca.uf_ref)
ORDER BY ca.cidade_ref, t.ano;

RESULTADO SUFICIENTE:
- Duas ou mais linhas por ano quando houver histórico.
- Se houver apenas um ano, responda com essa limitação.
""",

        "detalhamento_criterios": """
ESTRATÉGIA SQL: DETALHAMENTO DE CRITÉRIOS

Use quando o usuário pedir:
- critérios de uma cidade;
- pontos fortes e fracos;
- notas por indicador;
- descrição dos critérios.

FORMATO:
- Retorne detalhes necessários, mas evite excesso.
- Para pontos fortes/fracos, use ordenação por nota e limite.
- Para todos os critérios, limite de forma razoável.

MODELO PARA PONTOS FORTES:

SELECT
    cidade,
    estado,
    theme_pt AS tema,
    criteria_name_pt AS criterio,
    criteria_description_pt AS descricao,
    nota,
    ano
FROM top100_30
WHERE unaccent(upper(cidade::text)) = unaccent(upper('Cidade'))
  AND upper(estado::text) = upper('UF')
  AND nota IS NOT NULL
ORDER BY CAST(REPLACE(nota, ',', '.') AS NUMERIC) DESC
LIMIT 10;

MODELO PARA PONTOS FRACOS:

SELECT
    cidade,
    estado,
    theme_pt AS tema,
    criteria_name_pt AS criterio,
    criteria_description_pt AS descricao,
    nota,
    ano
FROM top100_30
WHERE unaccent(upper(cidade::text)) = unaccent(upper('Cidade'))
  AND upper(estado::text) = upper('UF')
  AND nota IS NOT NULL
ORDER BY CAST(REPLACE(nota, ',', '.') AS NUMERIC) ASC
LIMIT 10;

RESULTADO SUFICIENTE:
- Critérios retornados com tema, nome, descrição e nota.
- Não busque em outra tabela se a pergunta já foi respondida.
"""
    }

    return strategies.get(task_type, strategies["geral"] if "geral" in strategies else strategies["resumo_avaliacoes"])

toolkit = SQLDatabaseToolkit(db=db_bussola, llm=model)

db_tools = toolkit.get_tools()
# , "sql_db_schema", "sql_db_list_tables"
excluded_tool_names = ["sql_db_query_checker" , "sql_db_schema", "sql_db_list_tables"]   # Exclui ferramentas de consulta direta para forçar o uso do dicionário
db_tools_filtered = [
    tool for tool in db_tools 
    if tool.name not in excluded_tool_names
]
tools_agent = [store_memory_tool, retrieve_memories_tool, retrieve_last_ai_message_tool, retrieve_about] + db_tools
#tools_agent = [store_memory_tool, retrieve_memories_tool, retrieve_last_ai_message_tool, sql_db_query, retrieve_about, sql_db_schema]
tools_chat = [store_memory_tool, retrieve_memories_tool, retrieve_last_ai_message_tool, retrieve_about]
tools_rag = [retrieve_last_ai_message_tool]
tool_node = ToolNode(tools=tools_agent)