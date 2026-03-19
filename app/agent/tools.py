from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langgraph.prebuilt import ToolNode
from app.core.config import model, db_bussola


toolkit = SQLDatabaseToolkit(db=db_bussola, llm=model)

tools_agent = toolkit.get_tools()
tool_node = ToolNode(tools=tools_agent)


# @tool
# def consult_docs(query: str) -> str:
    
    