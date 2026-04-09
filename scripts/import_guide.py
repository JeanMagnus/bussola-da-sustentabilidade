import re
from langchain_core.documents import Document
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pinecone import Pinecone
from app.core.config import settings, embeddings, embeddings_large

# Ajuste de tamanho para o limite do Pinecone
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000, 
    chunk_overlap=500,
    separators=["\n## ", "\n### ", "\n- ", "\n| "]
)

def importar_dicionario_h2_correto():
    pc = Pinecone(api_key=settings.PINECONE_API_KEY)
    index = pc.Index(settings.PINECONE_INDEX_GUIDE_LARGE)
    
    # 1. Limpeza Segura
    print(f" Limpando namespace 'data_dictionary'...")
    try:
        index.delete(delete_all=True, namespace="data_dictionary")
        print(" Limpo.")
    except Exception:
        print(" Namespace já estava vazio.")

    # 2. Ler o arquivo completo
    with open("docs/guide/data-guide.md", "r", encoding="utf-8") as f:
        content = f.read()

    # 3. REGEX para Header 2 (##)
    # Procura por '## [Número] - [Nome].csv' até o próximo '##'
    # Esse padrão captura o nome, a descrição, a tabela markdown e as colunas (que são ###)
    pattern = r"## (\d+ - .*?\.csv)(.*?)(?=\n## |$)"
    matches = re.findall(pattern, content, re.DOTALL)

    documents = []
    for raw_title, body in matches:
        # Normalização do nome para o SQL (ex: "1 - CRITERIOS.csv" -> "CRITERIOS")
        table_name = raw_title.split("-")[-1].strip().replace(".csv", "").replace(" ", "_").lower()
        
        body_content = body.strip()
        # O corpo contém a descrição, a tabela e as colunas (Headers ###)
        chunks = text_splitter.split_text(body_content)
        
        for i, chunk in enumerate(chunks):
            full_text = f"TABELA REAL NO BANCO: {table_name}\n\n{chunk}"
            
            doc = Document(
                page_content=full_text,
                metadata={
                    "table_name": table_name,
                    "type": "dictionary",
                    "part": i + 1
                }
            )
            documents.append(doc)
        print(f"Indexando: {table_name} ({len(chunks)} partes)")

    # 4. Envio Final
    if documents:
        PineconeVectorStore.from_documents(
            documents=documents,
            embedding=embeddings_large,
            index_name=settings.PINECONE_INDEX_GUIDE_LARGE,
            namespace="data_dictionary"
        )
        print(f"\n SUCESSO! {len(matches)} tabelas mapeadas com sucesso.")
    else:
        print(" Nenhuma seção '## ... .csv' foi encontrada.")

if __name__ == "__main__":
    importar_dicionario_h2_correto()

# COMO RODAR NO DOCKER:
# docker compose exec api uv run env PYTHONPATH=/app python scripts/import_guide.py