from typing import Annotated, Sequence
from typing_extensions import TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph import add_messages

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    error_occurred: bool
    dictionary_rules: str
    is_dictionary_checked: bool
    intent: str
    dictionary_context: str
    sql_plan: str
    total_tokens: int
    input_tokens: int
    output_tokens: int
    last_msg_ai: str
    is_continuation: bool


    

