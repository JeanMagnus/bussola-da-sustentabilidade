from typing import Annotated, Sequence
from typing_extensions import TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph import add_messages
import operator


def overwrite_reducer(a, b):
    # Simplesmente sobrescreve o valor antigo com o novo
    return b

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    error_occurred: Annotated[bool, overwrite_reducer]
    dictionary_rules: str
    is_dictionary_checked: bool
    intent: str
    dictionary_context: str
    sql_plan: str
    # input_tokens: Annotated[int, operator.add]
    # output_tokens: Annotated[int, operator.add]
    # total_tokens: Annotated[int, operator.add]
    input_tokens: int
    output_tokens: int
    total_tokens: int
    last_msg_ai: str
    is_continuation: bool
    summary: str
    retries: int

    
