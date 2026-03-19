from app.core.config import model, db_bussola
from app.agent.state import AgentState
from app.agent.prompt import SYSTEM_PROMPT
from app.agent.tools import tools_agent
from app.core.config import trimmer
from langgraph.graph import END
from langchain.agents.middleware import before_model, after_model


async def agent(state: AgentState):
    prompt = SYSTEM_PROMPT
    messages_trimmer = trimmer.invoke([prompt] + state["messages"])
    model_with_tools = model.bind_tools(tools_agent)
    response = await model_with_tools.ainvoke(messages_trimmer)
    return {"messages": [response]}

# def should_continue(state: AgentState):
#     last_msg = state["messages"][-1]
#     if last_msg.tool_calls:
#         return "go_tools"
#     return END


def should_continue(state: AgentState):
    last_msg = state["messages"][-1]
    if hasattr(last_msg, "tool_calls") and last_msg.tool_calls:
        return "verify_sql"
    return "moderation_output"


@before_model(can_jump_to="END")
def moderation_input():
    return "check_relevance"

def check_relevance():
    return "agent"

def verify_sql():
    return "go_tools"

@after_model
def moderation_output():
    return END

