from langgraph.graph import StateGraph, START
from app.agent.state import AgentState
from app.agent.nodes import agent, should_continue
from app.agent.tools import tool_node

workflow = StateGraph(AgentState)

workflow.add_node("agent",agent)
workflow.add_node("go_tools", tool_node)



workflow.add_edge(START, "agent")
workflow.add_conditional_edges("agent", should_continue)
workflow.add_edge("go_tools", "agent")


