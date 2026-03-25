from pydantic import BaseModel


# Models do fastapi para entrada e saída de dados
class ChatInput(BaseModel):
    message: str
    thread_id: str = "default"
    user_id: str = "anonymous"

class ChatOutput(BaseModel):
    response: str
    thread_id: str
    user_id: str
    
    