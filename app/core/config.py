import os 
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import trim_messages
from langchain_openai.middleware import OpenAIModerationMiddleware
from langchain.agents import create_agent

load_dotenv()

class Settings:
    URI_DATABASE_BUSSOLA = os.getenv("URI_DATABASE_BUSSOLA")
    URI_DATABASE_CHECKPOIN = os.getenv("URI_DATABASE_CHECKPOINT")

    AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
    AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENTE")

settings = Settings()

db_bussola = SQLDatabase.from_uri(settings.URI_DATABASE_BUSSOLA)


model = AzureChatOpenAI(
    model = "gpt-5-nano",
    azure_deployment = settings.AZURE_OPENAI_DEPLOYMENT,
    api_version = settings.AZURE_OPENAI_API_VERSION,
    azure_endpoint = settings.AZURE_OPENAI_ENDPOINT,
    api_key = settings.AZURE_OPENAI_API_KEY,
    temperature = 0.7,

)

trimmer = trim_messages(
    max_tokens = 5000,
    strategy = "last",
    token_counter = model,
    include_system = True,
    start_on = "human",
    )


moderation = create_agent(
    model= model,
    middleware= [
        OpenAIModerationMiddleware(
            model= "omni-moderation-latest",
            check_input=True,
            check_output=True,
            check_tool_results=False,
            exit_behavior="end",
            violation_message=("Se liga!"
                               "Sua mensagem caiu na categoria: {categories}")
        )
    ]
)