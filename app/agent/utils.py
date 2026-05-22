import ast
import time
from contextlib import contextmanager
from app.agent.state import AgentState
from langchain_core.messages import ToolMessage, AIMessage, HumanMessage
import re
import unicodedata
from typing import Any
from sqlalchemy import inspect
from app.core.config import db_bussola
import json


# FUNÇÃO PARA CONTAGEM DE TOKENS POR NÓ
def token_count(response, node_name: str):
    if hasattr(response, "usage_metadata") and response.usage_metadata:
        usage = response.usage_metadata
        print(f"TOKENS USADOS NO NÓ {node_name}")
        print(f"   |-- Entrada (Prompt): {usage.get('input_tokens')}")
        print(f"   |-- Saída (Geração): {usage.get('output_tokens')}")
        print(f"   |-- Total da etapa: {usage.get('total_tokens')}")

# FUNÇÃO PARA CONTAGEM TOTAL DE TOKENS ACUMULADOS
def token_count_total(state, response):
    current_total = state.get("total_tokens", 0)
    current_input = state.get("input_tokens", 0)
    current_output = state.get("output_tokens", 0)

    if hasattr(response, "usage_metadata") and response.usage_metadata:
        usage = response.usage_metadata
        return {
            "total_tokens": current_total + usage.get("total_tokens", 0),
            "input_tokens": current_input + usage.get("input_tokens", 0),
            "output_tokens": current_output + usage.get("output_tokens", 0)
        }
    return { "total_tokens": current_total, "input_tokens": current_input, "output_tokens": current_output }

    # if hasattr(response, "usage_metadata") and response.usage_metadata:
    #     usage = response.usage_metadata
    #     return {
    #         "total_tokens": usage.get("total_tokens", 0),
    #         "input_tokens": usage.get("input_tokens", 0),
    #         "output_tokens": usage.get("output_tokens", 0)
    #     }
    # return { "total_tokens": 0, "input_tokens": 0, "output_tokens": 0 }

@contextmanager
def timer(node_name):
    start = time.perf_counter()
    yield
    end = time.perf_counter()
    print(f"LATÊNCIA DO NÓ [{node_name}]: {end - start:.2f}s")

def parse_sql_tool_result(raw_result: str):
    """
    Converte o resultado bruto da sql_db_query em uma estrutura genérica.
    Se vier como lista de tuplas, cria col_0, col_1, col_2...
    """

    if not raw_result:
        return []

    try:
        parsed = ast.literal_eval(raw_result)
    except Exception:
        return [{"value": raw_result}]

    if not isinstance(parsed, list):
        return [{"value": parsed}]

    rows = []

    for item in parsed:
        if isinstance(item, dict):
            rows.append(item)

        elif isinstance(item, tuple):
            row = {
                f"col_{idx}": value
                for idx, value in enumerate(item)
            }
            rows.append(row)

        else:
            rows.append({"value": item})

    return rows


def build_last_result_context_from_messages(state: AgentState):
    """
    Procura a última ToolMessage de sql_db_query e monta um contexto estruturado.
    Não cria nó novo. É chamada dentro do próprio agent.
    """

    messages = state.get("messages", [])

    tool_messages = [
        msg for msg in messages
        if isinstance(msg, ToolMessage)
    ]

    if not tool_messages:
        return {}

    last_tool_msg = tool_messages[-1]

    tool_name = getattr(last_tool_msg, "name", None)

    if tool_name != "sql_db_query":
        return {}

    raw_result = last_tool_msg.content
    rows = parse_sql_tool_result(raw_result)

    last_sql_query = state.get("last_sql_query")

    last_result_context = {
        "type": "sql_result",
        "source": "sql_db_query",
        "query": last_sql_query,
        "sql": last_sql_query,
        "row_count": len(rows),
        "rows": rows,
        "raw_result": raw_result,
        "description": "Último resultado SQL estruturado disponível para continuação."
    }

    print(f"   [MEMÓRIA] last_result_context atualizado com {len(rows)} linhas.")

    return {
        "last_sql_result": rows,
        "last_result_context": last_result_context,
    }


def normalize_text(text: Any) -> str:
    if text is None:
        return ""

    text = str(text).lower()
    text = unicodedata.normalize("NFD", text)

    text = "".join(
        char for char in text
        if unicodedata.category(char) != "Mn"
    )

    text = re.sub(r"\s+", " ", text)
    return text.strip()


def safe_model_dump(obj: Any) -> dict:
    """
    Garante que context_resolution funcione tanto como dict
    quanto como objeto Pydantic.
    """

    if obj is None:
        return {}

    if isinstance(obj, dict):
        return obj

    if hasattr(obj, "model_dump"):
        return obj.model_dump()

    return {}


def collect_required_values(context_resolution: Any) -> list[str]:
    """
    Coleta valores obrigatórios de context_resolution.referents.

    Exemplo:
    - Frei Rogério
    - Orléans
    - Urubici
    - Apodi
    - etc.

    Não coleta atributos como UF aqui, porque o principal é garantir
    que o agente não substitua a lista concreta por filtro genérico.
    """

    context_resolution = safe_model_dump(context_resolution)

    if not context_resolution:
        return []

    values = []

    referents = context_resolution.get("referents", [])

    for group in referents:
        if not isinstance(group, dict):
            continue

        must_preserve = group.get("must_preserve", False)

        if not must_preserve:
            continue

        group_values = group.get("values", [])

        for item in group_values:
            if isinstance(item, dict):
                value = item.get("value")

                if value:
                    values.append(str(value).strip())

            elif item:
                values.append(str(item).strip())

    unique_values = []

    for value in values:
        if value and value not in unique_values:
            unique_values.append(value)

    return unique_values


def sql_preserves_required_values(
    sql: str,
    required_values: list[str],
    threshold: float = 0.65,
) -> bool:
    """
    Verifica se a SQL preserva os valores obrigatórios.

    threshold=0.65 significa:
    - Se existem 14 valores obrigatórios, pelo menos 9 precisam aparecer na SQL.
    - Isso bloqueia consultas genéricas como WHERE _possui_gd = true.
    """

    if not required_values:
        return True

    sql_norm = normalize_text(sql)

    matched = 0

    for value in required_values:
        value_norm = normalize_text(value)

        if not value_norm:
            continue

        if value_norm in sql_norm:
            matched += 1
            continue

        tokens = [
            token for token in value_norm.split()
            if len(token) > 2
        ]

        if tokens:
            token_matches = sum(
                1 for token in tokens
                if token in sql_norm
            )

            token_ratio = token_matches / len(tokens)

            if token_ratio >= 0.8:
                matched += 1

    ratio = matched / len(required_values)

    print(f"   [VERIFY_SQL] Valores obrigatórios preservados: {matched}/{len(required_values)}")
    print(f"   [VERIFY_SQL] Taxa de preservação: {ratio:.2f}")

    return ratio >= threshold


CONTINUATION_MARKERS = (
    "elas", "eles", "essa", "esse", "essas", "esses", "isso", "isto",
    "delas", "deles", "dessa", "desse", "dessas", "desses", "nelas", "neles",
    "anteriores", "anterior", "acima", "citadas", "citados", "listadas", "listados",
    "primeiras", "primeiros", "últimas", "ultimas", "últimos", "ultimos",
)

QUESTION_STOPWORDS = {
    "a", "ao", "aos", "as", "com", "como", "da", "das", "de", "do", "dos",
    "e", "em", "entre", "na", "nas", "no", "nos", "o", "os", "ou", "para",
    "por", "qual", "quais", "que", "quem", "sao", "são", "seria", "seriam",
    "sobre", "tem", "ter", "um", "uma", "uns", "umas", "me", "mostre", "liste",
    "listar", "traga", "trazer", "diga", "informe", "dessas", "desses", "elas", "eles",
}




def _stringify_short(value: Any, max_chars: int = 80) -> str:
    value = str(value).strip()
    value = re.sub(r"\s+", " ", value)

    if len(value) > max_chars:
        value = value[: max_chars - 1].rstrip() + "…"

    return value


def _append_unique(items: list[str], value: Any, max_items: int) -> None:
    if len(items) >= max_items:
        return

    value_text = _stringify_short(value)

    if not value_text:
        return

    value_norm = normalize_text(value_text)

    if value_norm in {normalize_text(item) for item in items}:
        return

    items.append(value_text)


def extract_keywords_from_text(text: Any, max_keywords: int = 8) -> list[str]:
    """Extrai palavras-chave simples sem chamar modelo externo."""

    text_norm = normalize_text(text)

    if not text_norm:
        return []

    tokens = re.findall(r"[a-z0-9_]{3,}", text_norm)
    keywords: list[str] = []

    for token in tokens:
        if token in QUESTION_STOPWORDS:
            continue

        _append_unique(keywords, token, max_keywords)

        if len(keywords) >= max_keywords:
            break

    return keywords
def infer_entity_kind_from_column(column: str) -> str:
    col = str(column or "").lower()

    if col in ["cidade", "municipio", "município"]:
        return "cidade"

    if col in ["estado", "uf"]:
        return "estado"

    if col in ["criterio", "criteria_name_pt", "criteria_name_us", "criteria_name_es"]:
        return "criterio"

    if col in ["theme_pt", "theme_us", "theme_es", "theme"]:
        return "tema"

    if col in ["topic", "topic_description_pt"]:
        return "topico"

    if col in ["chave"]:
        return "chave"

    if col in ["codigo_municipio", "codigo", "codigo_ibge"]:
        return "codigo"

    return "valor"


def is_metric_column(key: str, value: Any) -> bool:
    col = str(key or "").lower()

    metric_names = [
        "nota",
        "media",
        "média",
        "media_geral",
        "media_tema",
        "total",
        "count",
        "quantidade",
        "qtd",
        "populacao",
        "pib",
        "idhm",
        "salario",
        "visitas",
        "aproveitamento",
    ]

    if any(name in col for name in metric_names):
        return True

    if isinstance(value, (int, float)):
        return True

    if isinstance(value, str) and re.fullmatch(r"[-+]?\d+(?:[,.]\d+)?", value.strip()):
        return True

    return False


def infer_datasets_from_query(query: str) -> list[str]:
    q = str(query or "").lower()

    known_tables = [
        "selo",
        "top100_30",
        "top100_15",
        "criterios",
        "ibge",
        "timeline_gd",
        "situacional_2023",
        "situacional_2023_pivot_median",
        "pivot_situacional",
        "destinations_2023",
        "remuneracao",
        "rais_geral",
    ]

    return [table for table in known_tables if table in q]


def infer_context_task(
    *,
    attributes: list[str],
    response_keywords: list[str],
    query: str = "",
) -> str:
    attrs = set(str(a).lower() for a in attributes)
    text = " ".join(response_keywords).lower()
    q = str(query or "").lower()

    if {"nota", "criterio", "criteria_name_pt", "theme_pt"} & attrs:
        return "avaliacao"

    if {"codigo_municipio", "regiao_intermediaria", "mesorregiao", "microrregiao"} & attrs:
        return "dados_geograficos"

    if "selo" in q or "certifica" in text or "green destinations" in text:
        return "certificacao"

    if "situacional" in q or any(a.startswith("q") for a in attrs):
        return "situacional"

    if "criterios" in q or "criteria_description_pt" in attrs:
        return "criterios"

    if "timeline" in q or "aproveitamento" in attrs:
        return "historico"

    return "consulta_sql"


def infer_operation_from_text(text: Any) -> str:
    t = str(text or "").lower()

    if any(k in t for k in ["compare", "comparação", "comparacao", "diferença", "diferenca"]):
        return "comparar"

    if any(k in t for k in ["ranking", "maiores", "menores", "ordenado", "ordem"]):
        return "ranquear"

    if any(k in t for k in ["média", "media", "avg"]):
        return "calcular_media"

    if any(k in t for k in ["liste", "lista", "quais", "mostre"]):
        return "listar"

    if any(k in t for k in ["explique", "significa", "descrição", "descricao"]):
        return "explicar"

    return "responder"


def infer_focus(
    *,
    entity_objects: list[dict[str, Any]],
    filters: dict[str, list[Any]],
    task: str,
) -> dict[str, Any]:
    priority = ["cidade", "criterio", "tema", "estado", "codigo", "chave"]

    for kind in priority:
        values = [
            e["value"]
            for e in entity_objects
            if e.get("kind") == kind and e.get("value")
        ]

        if values:
            return {
                "kind": kind,
                "values": list(dict.fromkeys(values))[:10],
                "label": f"foco anterior inferido para tarefa {task}",
            }

    if filters:
        first_key = next(iter(filters.keys()))
        return {
            "kind": first_key,
            "values": filters[first_key][:10],
            "label": f"foco anterior inferido por filtro para tarefa {task}",
        }

    return {
        "kind": "unknown",
        "values": [],
        "label": "nenhum foco claro inferido",
    }

def build_lightweight_context(
    *,
    last_ai_message: Any = "",
    last_result_context: Any = None,
    max_entities: int = 20,
) -> dict[str, Any]:
    result_context = last_result_context if isinstance(last_result_context, dict) else {}
    rows = result_context.get("rows") or []
    query = result_context.get("query", "")
    columns = result_context.get("columns") or []

    entities: list[str] = []
    attributes: list[str] = []
    entity_objects: list[dict[str, Any]] = []
    metrics: list[dict[str, Any]] = []
    filters: dict[str, list[Any]] = {}

    for row in rows[:max_entities]:
        if isinstance(row, dict):
            for key in row.keys():
                _append_unique(attributes, key, 20)

            for key, value in row.items():
                if not isinstance(value, str):
                    continue

                value = value.strip()

                if not value:
                    continue

                if re.fullmatch(r"[-+]?\d+(?:[,.]\d+)?", value):
                    continue
                
                if value.lower().startswith(("http://", "https://")):
                    continue

                kind = infer_entity_kind_from_column(key)

                _append_unique(entities, value, max_entities)

                entity_obj = {
                    "kind": kind,
                    "value": value,
                    "source_column": key,
                }

                attrs = {}
                for attr_key in ["estado", "uf", "ano", "codigo_municipio", "criterio", "theme_pt"]:
                    if attr_key in row and row[attr_key] not in (None, "", "nan"):
                        attrs[attr_key] = row[attr_key]

                if attrs:
                    entity_obj["attributes"] = attrs

                if entity_obj not in entity_objects:
                    entity_objects.append(entity_obj)

            for key, value in row.items():
                if is_metric_column(key, value):
                    metrics.append({
                        "name": key,
                        "value": value,
                    })

            for key in ["cidade", "estado", "uf", "ano", "criterio", "theme_pt", "codigo_municipio"]:
                if key in row and row[key] not in (None, "", "nan"):
                    filters.setdefault(key, [])
                    if row[key] not in filters[key]:
                        filters[key].append(row[key])

        else:
            _append_unique(entities, row, max_entities)

        if len(entities) >= max_entities:
            break

    response_keywords = extract_keywords_from_text(last_ai_message, max_keywords=8)

    datasets = infer_datasets_from_query(query)
    task = infer_context_task(
        attributes=attributes,
        response_keywords=response_keywords,
        query=query,
    )
    operation = infer_operation_from_text(last_ai_message)

    focus = infer_focus(
        entity_objects=entity_objects,
        filters=filters,
        task=task,
    )

    return {
        "type": "lightweight_previous_turn_context",

        "task": task,
        "operation": operation,
        "focus": focus,
        "entity_objects": entity_objects[:max_entities],
        "datasets": datasets,
        "metrics": metrics[:12],
        "filters": filters,
        "result_summary": {
            "row_count": result_context.get("row_count", len(rows) if rows else 0),
            "sample_size": min(len(rows), max_entities) if rows else 0,
            "columns": attributes[:20],
        },
        "entities": entities,
        "attributes": attributes,
        "response_keywords": response_keywords,
        "row_count": result_context.get("row_count", len(rows) if rows else 0),
        "source": result_context.get("source", "last_ai_message" if last_ai_message else "none"),
    }

def build_resolved_question_generic(
    *,
    user_text: str,
    previous_context: dict | None,
) -> str:
    if not previous_context:
        return user_text

    compact_context = {
        "task": previous_context.get("task"),
        "operation": previous_context.get("operation"),
        "focus": previous_context.get("focus"),
        "datasets": previous_context.get("datasets"),
        "attributes": previous_context.get("attributes", [])[:20],
        "metrics": previous_context.get("metrics", [])[:10],
        "filters": previous_context.get("filters"),
        "entities": previous_context.get("entity_objects", [])[:15],
        "row_count": previous_context.get("row_count"),
    }

    return f"""
A pergunta atual é uma continuação da interação anterior.

Pergunta original atual:
{user_text}

Contexto estruturado anterior:
{compact_context}

Tarefa:
Responda à pergunta atual preservando o contexto anterior.
Se o usuário pedir comparação, compare a nova entidade com o foco anterior.
Se o usuário pedir filtro, tabela, ordenação, resumo ou detalhe, aplique isso sobre o foco anterior.
Não trate a pergunta atual como isolada.
"""

def build_tool_error_messages(last_msg, error_content: str) -> list[ToolMessage]:
    """
    Quando bloqueamos uma tool call antes de executar,
    precisamos devolver ToolMessage para cada tool_call existente.

    Isso evita erro de sequência:
    AIMessage com tool_calls precisa ser seguido por ToolMessage.
    """

    tool_messages = []

    if not hasattr(last_msg, "tool_calls") or not last_msg.tool_calls:
        return tool_messages

    for tool_call in last_msg.tool_calls:
        tool_messages.append(
            ToolMessage(
                tool_call_id=tool_call["id"],
                name=tool_call["name"],
                content=error_content,
            )
        )

    return tool_messages


def detect_continuation_question(
    user_text: str,
    previous_context: dict | None,
) -> bool:
    if not previous_context:
        return False

    text = str(user_text or "").lower().strip()

    if not text:
        return False

    continuation_markers = [
        "compare com",
        "comparar com",
        "e com",
        "agora com",
        "em relação a",
        "em relacao a",
        "dessas",
        "desses",
        "dessa",
        "desse",
        "essas",
        "esses",
        "isso",
        "isto",
        "elas",
        "eles",
        "respectivos",
        "respectivas",
        "dados anteriores",
        "resultado anterior",
        "lista anterior",
        "da lista",
        "com a cidade",
        "com o município",
        "com o municipio",
        "filtre por",
        "ordene por",
        "mostre só",
        "mostre apenas",
        "faça uma tabela",
        "transforme em tabela",
        "explique melhor",
        "detalhe",
        "resuma",
    ]

    if any(marker in text for marker in continuation_markers):
        return True

    short_followup_verbs = [
        "compare",
        "detalhe",
        "resuma",
        "explique",
        "liste",
        "ordene",
        "filtre",
        "mostre",
    ]

    words = text.split()

    if len(words) <= 6 and any(v in text for v in short_followup_verbs):
        return True

    return False


COLUMN_ALIASES = {
    "atividade_turistica": {
        "municã­pio": "municipio",
        "o_municã­pio_possui_legislaã§ã£o_relacionada_ao_turismo?": "possui_legislacao_turismo",
        "o_municã­pio_possui_plano_municipal_de_turismo_e_/ou_plano_de": "possui_plano_turismo",
        "nâº_de_hospedagem": "num_hospedagem",
        "nâº_de_leitos": "num_leitos",
        "possui_guias_e/ou_condutores_de_turismo?": "possui_guias_turismo",
    }
}

_SCHEMA_CACHE: str | None = None

def get_schema_string() -> str:
    global _SCHEMA_CACHE
    if _SCHEMA_CACHE:
        return _SCHEMA_CACHE

    inspector = inspect(db_bussola._engine)
    tables = inspector.get_table_names()
    lines = []

    for table in tables:
        cols = inspector.get_columns(table)
        pk_cols = inspector.get_pk_constraint(table).get("constrained_columns", [])
        table_aliases = COLUMN_ALIASES.get(table, {})

        col_strs = []
        for c in cols:
            raw_name = c["name"]
            alias = table_aliases.get(raw_name)

            if alias:
                col_str = f"{alias} [use este nome] ({c['type']})"
            else:
                is_pk = "*" if raw_name in pk_cols else ""
                col_str = f"{raw_name}{is_pk} ({c['type']})"

            col_strs.append(col_str)

        lines.append(f"• {table}: {', '.join(col_strs)}")

    _SCHEMA_CACHE = "\n".join(lines)
    return _SCHEMA_CACHE
