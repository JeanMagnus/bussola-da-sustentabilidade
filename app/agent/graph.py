from langgraph.graph import StateGraph, START, END
from app.agent.state import AgentState
from app.agent.nodes import agent, classify_intent, dictionary_lookup, dictionary_retrieval, route_classify_intent, setup_node, guardrail_input, route_guardrail_input, should_continue, moderation_input, check_relevance, moderation_output, verify_sql, route_check_relevance, route_moderation_input, route_verify_sql, route_moderation_output, summarization_node
from app.agent.tools import tool_node

workflow = StateGraph(AgentState)

workflow.add_node("setup_node", setup_node)
workflow.add_node("guardrail_input", guardrail_input)
workflow.add_node("agent", agent)
workflow.add_node("summarization_node", summarization_node)
workflow.add_node("go_tools", tool_node)
#workflow.add_node("moderation_input", moderation_input)
#workflow.add_node("check_relevance", check_relevance)
workflow.add_node("moderation_output", moderation_output)
workflow.add_node("verify_sql", verify_sql)
#workflow.add_node("dictionary_lookup", dictionary_lookup)
workflow.add_node("dictionary_retrieval", dictionary_retrieval)
workflow.add_node("classify_intent", classify_intent)


workflow.add_edge(START, "setup_node")
workflow.add_edge("setup_node", "summarization_node")
#workflow.add_edge("summarization_node", "moderation_input")
workflow.add_edge("summarization_node", "guardrail_input")
#workflow.add_edge("dictionary_lookup", "agent")
workflow.add_edge("go_tools", "agent")
workflow.add_edge("moderation_output", END)
workflow.add_edge("dictionary_retrieval", "agent")

# workflow.add_conditional_edges("moderation_input", route_moderation_input,
#                                {
#                                    "check_relevance": "check_relevance",
#                                    END: END
#                                })
# workflow.add_conditional_edges("check_relevance", route_check_relevance,
#                                {
#                                    "agent": "agent",
#                                    END: END
#                                })

workflow.add_conditional_edges("guardrail_input", route_guardrail_input,
                                {
                                    #"agent": "agent", 
                                    "classify_intent": "classify_intent",
                                    END: END          
                                }
                                )

workflow.add_conditional_edges("classify_intent", route_classify_intent,
                               {
                                   "dictionary_retrieval": "dictionary_retrieval",
                                   "agent": "agent"
                               }
                               )

workflow.add_conditional_edges("agent", should_continue,
                               {
                                   #"dictionary_lookup": "dictionary_lookup",
                                   "verify_sql": "verify_sql",
                                   "go_tools": "go_tools",
                                   "moderation_output": "moderation_output",
                                    END: END
                               }
                               )
workflow.add_conditional_edges("verify_sql", route_verify_sql,
                               {
                                   "go_tools": "go_tools",
                                   END: END
                               }
                               )
workflow.add_conditional_edges("moderation_output", route_moderation_output,
                               {
                                   "agent": "agent",
                                   END: END
                               }
                               )