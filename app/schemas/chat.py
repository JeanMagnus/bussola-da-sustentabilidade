from pydantic import BaseModel

class ChatInput(BaseModel):
    message: str
    thread_id: str = "default"

class ChatOutput(BaseModel):
    response: str
    thread_id: str
    