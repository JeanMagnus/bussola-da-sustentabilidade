from app.core.config import model, db_bussola
from app.agent.state import AgentState
from app.agent.prompt import SYSTEM_PROMPT
from app.agent.tools import tools_agent
from app.core.config import trimmer
from langgraph.graph import END

async def agent(state: AgentState):
    prompt = SYSTEM_PROMPT
    messages_trimmer = trimmer.invoke([prompt] + state["messages"])
    model_with_tools = model.bind_tools(tools_agent)
    response = await model_with_tools.ainvoke(messages_trimmer)
    return {"messages": [response]}

def should_continue(state: AgentState):
    last_msg = state["messages"][-1]
    if last_msg.tool_calls:
        return "go_tools"
    return END

