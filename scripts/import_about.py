import re
from langchain_core.documents import Document
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pinecone import Pinecone
from app.core.config import settings, embeddings_large

# Separadores focados em estrutura de texto e listas
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, # Menor para textos institucionais serem mais diretos
    chunk_overlap=200,
    separators=["\n## ", "\n### ", "\n- ", "\n\n"]
)

def importar_conteudo_about():
    pc = Pinecone(api_key=settings.PINECONE_API_KEY)
    index = pc.Index(settings.PINECONE_INDEX_ABOUT)
    
    namespace = "about"
    
    print(f"Limpando namespace '{namespace}'...")
    try:
        # Tenta deletar todos os vetores do namespace
        index.delete(delete_all=True, namespace=namespace)
        print("Namespace limpo com sucesso.")
    except Exception as e:
        # Se o erro for 404 (NotFound), significa que o namespace não existe, o que é esperado na primeira execução
        if "404" in str(e) or "not found" in str(e).lower():
            print(f"Namespace '{namespace}' não encontrado. Criando um novo...")
        else:
            # Caso seja outro erro (falha de conexão, etc), você ainda quer saber
            print(f"Erro ao tentar limpar o namespace: {e}")

    with open("docs/about/about.md", "r", encoding="utf-8") as f:
        content = f.read()

    # REGEX Adaptado: Captura o Título (H1 ou H2) e tudo até o próximo título igual ou fim do arquivo
    # Funciona para: # Titulo Principal ou ## Subtitulo
    pattern = r"(?:^|\n)(#+ .*?)(?=\n#+ |$)"
    matches = re.findall(pattern, content, re.DOTALL)

    documents = []
    for section in matches:
        # Extrai a primeira linha como título da seção
        lines = section.strip().split('\n')
        section_title = lines[0].replace('#', '').strip()
        body_content = "\n".join(lines[1:]).strip()
        
        chunks = text_splitter.split_text(body_content)
        
        for i, chunk in enumerate(chunks):
            # Injetamos o contexto da seção em cada pedaço
            full_text = f"CONTEXTO: {section_title}\n\n{chunk}"
            
            doc = Document(
                page_content=full_text,
                metadata={
                    "section": section_title,
                    "type": "institutional_info",
                    "part": i + 1
                }
            )
            documents.append(doc)
        print(f"Indexando Seção: {section_title} ({len(chunks)} partes)")

    if documents:
        PineconeVectorStore.from_documents(
            documents=documents,
            embedding=embeddings_large,
            index_name=settings.PINECONE_INDEX_ABOUT,
            namespace=namespace
        )
        print(f"\n SUCESSO! {len(documents)} enviados.")

if __name__ == "__main__":
    importar_conteudo_about()

# COMO RODAR NO DOCKER:
# docker compose exec api uv run env PYTHONPATH=/app python scripts/import_about.py