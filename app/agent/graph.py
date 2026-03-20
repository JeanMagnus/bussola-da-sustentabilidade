from langgraph.graph import StateGraph, START, END
from app.agent.state import AgentState
from app.agent.nodes import agent, should_continue, moderation_input, check_relevance, moderation_output, verify_sql, route_check_relevance, route_moderation_input, route_verify_sql
from app.agent.tools import tool_node

workflow = StateGraph(AgentState)

workflow.add_node("agent", agent)
workflow.add_node("go_tools", tool_node)
workflow.add_node("moderation_input", moderation_input)
workflow.add_node("check_relevance", check_relevance)
workflow.add_node("moderation_output", moderation_output)
workflow.add_node("verify_sql", verify_sql)


workflow.add_edge(START, "moderation_input")

workflow.add_conditional_edges("moderation_input", route_moderation_input)
workflow.add_conditional_edges("check_relevance", route_check_relevance)
workflow.add_conditional_edges("agent", should_continue)
workflow.add_conditional_edges("verify_sql", route_verify_sql)

workflow.add_edge("go_tools", "agent")
workflow.add_edge("moderation_output", END)





