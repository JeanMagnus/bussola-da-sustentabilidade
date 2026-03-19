import fitz  # PyMuPDF
import os

def converter_pdf_para_md_leve(pdf_path, md_path):
    if not os.path.exists(pdf_path):
        print(f"Erro: Arquivo {pdf_path} não encontrado.")
        return

    print(f"--- Convertendo {pdf_path} de forma leve ---")
    
    # Abre o documento
    doc = fitz.open(pdf_path)
    markdown_content = ""

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        # Extrai o texto já tentando formatar blocos
        text = page.get_text("text")
        markdown_content += f"\n\n## Página {page_num + 1}\n\n"
        markdown_content += text

    # Salva o resultado
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    
    print(f"--- Sucesso! Arquivo salvo em: {md_path} ---")

if __name__ == "__main__":
    PDF_INPUT = "docs/guide/data-guide.pdf"
    MD_OUTPUT = "docs/guide/new-data-guide.md"
    converter_pdf_para_md_leve(PDF_INPUT, MD_OUTPUT)