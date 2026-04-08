
import time
from contextlib import contextmanager

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

@contextmanager
def timer(node_name):
    start = time.perf_counter()
    yield
    end = time.perf_counter()
    print(f"LATÊNCIA DO NÓ [{node_name}]: {end - start:.2f}s")