import ast
import time
from contextlib import contextmanager
from app.agent.state import AgentState
from langchain_core.messages import ToolMessage
import re
import unicodedata
from typing import Any

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


def is_likely_continuation_question(text: Any) -> bool:
    """
    Heurística barata para detectar perguntas que dependem do turno anterior.

    Evita uma chamada extra ao LLM quando a mensagem usa pronomes ou expressões
    típicas de continuação ("dessas", "e elas?", "quais são os códigos?").
    """

    text_norm = normalize_text(text)

    if not text_norm:
        return False

    if any(re.search(rf"\b{re.escape(marker)}\b", text_norm) for marker in CONTINUATION_MARKERS):
        return True

    continuation_prefixes = (
        "e ", "mas ", "tambem ", "também ", "agora ", "alem disso ", "além disso ",
        "quanto a ", "quanto ao ", "no caso ", "nesse caso ", "neste caso ",
    )

    if text_norm.startswith(continuation_prefixes):
        return True

    short_follow_up_patterns = (
        r"^quais( sao| são)?\b",
        r"^qual( e| é)?\b",
        r"^quant[ao]s?\b",
        r"^liste\b",
        r"^mostre\b",
        r"^compare\b",
        r"^detalhe\b",
        r"^explique\b",
    )

    return len(text_norm.split()) <= 8 and any(
        re.search(pattern, text_norm)
        for pattern in short_follow_up_patterns
    )


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


def build_lightweight_context(
    *,
    last_ai_message: Any = "",
    last_result_context: Any = None,
    max_entities: int = 20,
) -> dict[str, Any]:
    """
    Monta uma memória de estado compacta com os principais atributos do turno anterior.

    Essa estrutura substitui a antiga resolução contextual via LLM no nó RAG:
    ela reaproveita entidades/atributos do último resultado SQL e poucas palavras
    da resposta final, mantendo o contexto barato e previsível.
    """

    result_context = last_result_context if isinstance(last_result_context, dict) else {}
    rows = result_context.get("rows") or []

    entities: list[str] = []
    attributes: list[str] = []

    for row in rows[:max_entities]:
        if isinstance(row, dict):
            for key in row.keys():
                _append_unique(attributes, key, 12)

            preferred_values = [
                value for value in row.values()
                if isinstance(value, str)
                and value.strip()
                and not re.fullmatch(r"[-+]?\d+(?:[,.]\d+)?", value.strip())
            ]

            for value in preferred_values:
                _append_unique(entities, value, max_entities)
                if len(entities) >= max_entities:
                    break
        else:
            _append_unique(entities, row, max_entities)

        if len(entities) >= max_entities:
            break

    response_keywords = extract_keywords_from_text(last_ai_message, max_keywords=8)

    return {
        "type": "lightweight_previous_turn_context",
        "entities": entities,
        "attributes": attributes,
        "response_keywords": response_keywords,
        "row_count": result_context.get("row_count", len(rows) if rows else 0),
        "source": result_context.get("source", "last_ai_message" if last_ai_message else "none"),
    }


def build_search_query_from_state(user_question: Any, previous_context: Any) -> str:
    """
    Conecta a pergunta atual aos principais atributos do estado anterior para o Pinecone.
    """

    context = previous_context if isinstance(previous_context, dict) else {}
    terms: list[str] = []

    for keyword in extract_keywords_from_text(user_question, max_keywords=8):
        _append_unique(terms, keyword, 14)

    for attribute in context.get("attributes", [])[:6]:
        _append_unique(terms, attribute, 14)

    for keyword in context.get("response_keywords", [])[:4]:
        _append_unique(terms, keyword, 14)

    for entity in context.get("entities", [])[:4]:
        _append_unique(terms, entity, 14)

    return " ".join(terms).strip()


def build_context_resolution_from_state(user_question: Any, previous_context: Any) -> dict[str, Any] | None:
    """
    Cria uma resolução contextual compatível com o schema existente sem chamada LLM.
    """

    context = previous_context if isinstance(previous_context, dict) else {}
    entities = context.get("entities", []) or []

    if not entities and not context.get("attributes"):
        return None

    referents = []

    if entities:
        referents.append(
            {
                "label": "itens do resultado anterior",
                "kind_hint": "previous_result_item",
                "values": [
                    {"value": entity, "attributes": {}}
                    for entity in entities
                ],
                "expected_count": context.get("row_count") or len(entities),
                "source": "last_sql_result" if context.get("source") == "sql_db_query" else "last_ai_message",
                "must_preserve": True,
            }
        )

    search_query = build_search_query_from_state(user_question, context)
    rewritten_parts = [str(user_question).strip()]

    if entities:
        rewritten_parts.append("considerando os itens anteriores: " + ", ".join(entities[:10]))

    return {
        "is_context_dependent": True,
        "rewritten_question": "; ".join(rewritten_parts),
        "referents": referents,
        "requested_outputs": extract_keywords_from_text(user_question, max_keywords=6),
        "operation": "follow_up",
        "search_query": search_query or str(user_question).strip(),
    }


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