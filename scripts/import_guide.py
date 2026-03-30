import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from app.core.config import settings, embeddings

# 1. Carregar o arquivo enviado (data-guide.md)
loader = TextLoader("docs/guide/data-guide.md")
documento = loader.load()

# 2. Definir a estratégia de divisão baseada nos cabeçalhos
# Isso preserva a relação entre "Tabela X" e suas "Colunas"
headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"), # Nível onde estão os nomes das tabelas (ex: 1 - CRITERIOS.csv)
]

splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
chunks = splitter.split_text(documento[0].page_content)


# 4. Enviar para o Pinecone
index_name = settings.PINECONE_INDEX_GUIDE

add_doc_vector_store = PineconeVectorStore.from_documents(
    pinecone_api_key=settings.PINECONE_API_KEY,
    documents=chunks,
    embedding=embeddings,
    index_name=index_name,
    namespace="data_dictionary" # Opcional: use namespaces para organizar
)

print(f"Sucesso! {len(chunks)} seções do dicionário foram indexadas.")


# COMO RODAR NO DOCKER:
# docker compose exec api uv run env PYTHONPATH=/app python scripts/import_guide.py