import os
import sys
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.vectorstores import FAISS

sys.path.append(os.getcwd())

from app.core.config import settings

# 1. Carregar variáveis do arquivo .env
load_dotenv()

def create_pdf_vector_db():

    api_key = settings.AZURE_OPENAI_API_KEY
    endpoint = settings.AZURE_OPENAI_ENDPOINT
    api_version = settings.AZURE_OPENAI_API_VERSION
    embedding_deployment = settings.AZURE_OPENAI_DEPLOYMENT


    pdf_path = "docs/guide/data-guide.pdf" # Caminho para o seu arquivo
    if not os.path.exists(pdf_path):
        print(f"Erro: O arquivo {pdf_path} não foi encontrado.")
        return

    print(f"--- Carregando PDF: {pdf_path} ---")
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    # 3. Divisão em Chunks (Igual à lógica do vídeo do RAG)
    # Chunk size de 1000 com overlap de 200 para manter o contexto
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
    )
    all_splits = text_splitter.split_documents(docs)
    print(f"PDF dividido em {len(all_splits)} pedaços de texto.")

    # 4. Configuração dos Embeddings da Azure
    print("--- Gerando Embeddings na Azure ---")
    embeddings = AzureOpenAIEmbeddings(
        azure_deployment=embedding_deployment,
        openai_api_key=api_key,
        azure_endpoint=endpoint,
        api_version=api_version
    )

    # 5. Criação do Banco Vetorial e Persistência Local (FAISS)
    # Isso cria o índice comparando os textos e salva em uma pasta
    print("--- Criando índice FAISS local ---")
    vector_store = FAISS.from_documents(documents=all_splits, embedding=embeddings)
    
    # Nome da pasta onde o índice será salvo
    index_folder = "bussola_index"
    vector_store.save_local(index_folder)

    print(f"--- SUCESSO! Índice salvo na pasta: {index_folder} ---")
    print("Agora você pode carregar este índice na sua Tool do LangGraph.")

if __name__ == "__main__":
    create_pdf_vector_db()