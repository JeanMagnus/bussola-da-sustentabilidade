
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

        # Caso direto: "sao miguel do gostoso" aparece na SQL
        if value_norm in sql_norm:
            matched += 1
            continue

        # Fallback para nomes compostos
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