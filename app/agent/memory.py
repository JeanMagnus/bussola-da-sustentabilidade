
from typing import Literal
from pydantic import BaseModel
from langchain_pinecone import PineconeVectorStore
from app.core.config import embeddings,embeddings_large, settings


class Memory(BaseModel):
    content: str
    memory_type: Literal["episodic", "semantic"]    


vector_store = PineconeVectorStore(
    index_name=settings.PINECONE_INDEX_NAME,
    embedding=embeddings,
    pinecone_api_key=settings.PINECONE_API_KEY, 
)

guide_vector_store = PineconeVectorStore(
    index_name=settings.PINECONE_INDEX_GUIDE,
    embedding=embeddings,
    pinecone_api_key=settings.PINECONE_API_KEY,
    namespace="data_dictionary" 
)

guide_vector_store_large = PineconeVectorStore(
    index_name=settings.PINECONE_INDEX_GUIDE_LARGE,
    embedding=embeddings_large,
    pinecone_api_key=settings.PINECONE_API_KEY,
    namespace="data_dictionary"
)
