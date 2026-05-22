from langgraph.graph import StateGraph, START, END
from app.agent.state import AgentState
from app.agent.nodes import (
    agent,
    classify_intent,
    context_resolution_node,
    fallback_node,
    rag_agent,
    route_classify_intent,
    setup_node,
    guardrail_input,
    route_guardrail_input,
    should_continue,
    moderation_output,
    verify_sql,
    route_verify_sql,
    route_moderation_output,
    summarization_node,
)
from app.agent.tools import tool_node


workflow = StateGraph(AgentState)

workflow.add_node("setup_node", setup_node)
workflow.add_node("guardrail_input", guardrail_input)
workflow.add_node("classify_intent", classify_intent)
#workflow.add_node("rag_agent", rag_agent)
workflow.add_node("agent", agent)
workflow.add_node("verify_sql", verify_sql)
workflow.add_node("go_tools", tool_node)
workflow.add_node("moderation_output", moderation_output)
workflow.add_node("fallback_node", fallback_node)
workflow.add_node("summarization_node", summarization_node)
workflow.add_node("context_resolution_node", context_resolution_node)
#workflow.add_node("answer_generation_node", answer_generation_node)


workflow.add_edge(START, "setup_node")
workflow.add_edge("setup_node", "guardrail_input")

workflow.add_conditional_edges(
    "guardrail_input",
    route_guardrail_input,
    {
        "classify_intent": "context_resolution_node",
        END: "summarization_node",
    },
)

workflow.add_edge("context_resolution_node", "classify_intent")
workflow.add_edge("classify_intent", "agent")

# workflow.add_conditional_edges(
#     "classify_intent",
#     route_classify_intent,
#     {
#         "rag_agent": "rag_agent",
#         "agent": "agent",
#     },
# )

#workflow.add_edge("rag_agent", "agent")

workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "verify_sql": "verify_sql",
        "go_tools": "go_tools",
        "moderation_output": "moderation_output",
        "fallback_node": "fallback_node",
        END: "summarization_node",
    },
)

workflow.add_conditional_edges(
    "verify_sql",
    route_verify_sql,
    {
        "go_tools": "go_tools",
        "agent": "agent",
        END: "summarization_node",
    },
)

workflow.add_edge("go_tools", "agent")

workflow.add_edge("fallback_node", "agent")

workflow.add_conditional_edges(
    "moderation_output",
    route_moderation_output,
    {
        "agent": "agent",
        "summarization_node": "summarization_node",
    },
)
#workflow.add_edge("answer_generation_node", "summarization_node")
workflow.add_edge("summarization_node", END)
