import os 
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from langchain_core.messages import trim_messages
from langchain_openai.middleware import OpenAIModerationMiddleware
from langchain.agents import create_agent
from langchain_groq import ChatGroq

load_dotenv()

class Settings:
    URI_DATABASE_BUSSOLA = os.getenv("URI_DATABASE_BUSSOLA")
    URI_DATABASE_CHECKPOIN = os.getenv("URI_DATABASE_CHECKPOINT")

    AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
    AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENTE")

    AZURE_OPENAI_EMBEDDING_DEPLOYMENT = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")
    AZURE_OPENAI_EMBEDDING_API_VERSION = os.getenv("AZURE_OPENAI_EMBEDDING_API_VERSION")
    AZURE_OPENAI_EMBEDDING_ENDPOINT = os.getenv("AZURE_OPENAI_EMBEDDING_ENDPOINT")
    AZURE_OPENAI_EMBEDDING_API_KEY = os.getenv("AZURE_OPENAI_EMBEDDING_API_KEY")

    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
    PINECONE_INDEX_GUIDE = os.getenv("PINECONE_INDEX_GUIDE")

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    AZURE_DEEPSEEK_API_KEY = os.getenv("AZURE_DEEPSEEK_API_KEY")
    AZURE_DEEPSEEK_ENDPOINT = os.getenv("AZURE_DEEPSEEK_ENDPOINT")
    AZURE_DEEPSEEK_API_VERSION = os.getenv("AZURE_DEEPSEEK_API_VERSION")
    AZURE_DEEPSEEK_DEPLOYMENT = os.getenv("AZURE_DEEPSEEK_DEPLOYMENT")

settings = Settings()

db_bussola = SQLDatabase.from_uri(settings.URI_DATABASE_BUSSOLA)


rag_model = AzureChatOpenAI(
    model = "gpt-5-nano",
    azure_deployment = settings.AZURE_OPENAI_DEPLOYMENT,
    api_version = settings.AZURE_OPENAI_API_VERSION,
    azure_endpoint = settings.AZURE_OPENAI_ENDPOINT,
    api_key = settings.AZURE_OPENAI_API_KEY,
    temperature = 0,
    max_tokens = 1500,
)

model = AzureChatOpenAI(
    model = "gpt-5-nano",
    azure_deployment = settings.AZURE_OPENAI_DEPLOYMENT,
    api_version = settings.AZURE_OPENAI_API_VERSION,
    azure_endpoint = settings.AZURE_OPENAI_ENDPOINT,
    api_key = settings.AZURE_OPENAI_API_KEY,
    temperature = 0,
)

deepseek_model = AzureChatOpenAI(
    model = "deepseek-v3.2",
    azure_deployment = settings.AZURE_DEEPSEEK_DEPLOYMENT,
    api_version = settings.AZURE_DEEPSEEK_API_VERSION,
    azure_endpoint = settings.AZURE_DEEPSEEK_ENDPOINT,
    api_key = settings.AZURE_DEEPSEEK_API_KEY,
    temperature = 0,
)

# summarizer_model = AzureChatOpenAI(
#     model = "gpt-5-nano",
#     azure_deployment = settings.AZURE_OPENAI_DEPLOYMENT,
#     api_version = settings.AZURE_OPENAI_API_VERSION,
#     azure_endpoint = settings.AZURE_OPENAI_ENDPOINT,
#     api_key = settings.AZURE_OPENAI_API_KEY,
#     temperature = 0,
# )

summarizer_model = ChatGroq(
    model = "llama-3.1-8b-instant",
    groq_api_key = settings.GROQ_API_KEY,
    temperature = 0
)


moderation_model = ChatGroq(
    model = "openai/gpt-oss-safeguard-20b",
    groq_api_key = settings.GROQ_API_KEY,
    temperature = 0
)

# Fallback model para garantir que o agente continue funcionando mesmo se o modelo principal tiver problemas.
# backup_model = AzureChatOpenAI(
#     model = "gpt-5-mini",
#     azure_deployment = settings.AZURE_OPENAI_DEPLOYMENT,
#     api_version = settings.AZURE_OPENAI_API_VERSION,
#     azure_endpoint = settings.AZURE_OPENAI_ENDPOINT,
#     api_key = settings.AZURE_OPENAI_API_KEY,
#     temperature = 0,
# )

embeddings = AzureOpenAIEmbeddings(
    model = "text-embedding-3-small",
    azure_deployment = settings.AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
    api_version = settings.AZURE_OPENAI_EMBEDDING_API_VERSION,
    azure_endpoint = settings.AZURE_OPENAI_EMBEDDING_ENDPOINT,
    api_key = settings.AZURE_OPENAI_EMBEDDING_API_KEY,
)

trimmer = trim_messages(
    max_tokens = 3000,
    strategy = "last",
    token_counter = model,
    include_system = True,
    allow_partial = False,
    start_on = "human",
    )


# moderation = create_agent(
#     model= model,
#     middleware= [
#         OpenAIModerationMiddleware(
#             model= "omni-moderation-latest",
#             check_input=True,
#             check_output=True,
#             check_tool_results=False,
#             exit_behavior="end",
#             violation_message=("Se liga!"
#                                "Sua mensagem caiu na categoria: {categories}")
#         )


#     ]
# )
