import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()


# Configurações de Ambiente
PATH_CSV = 'docs/database'
URI_DATABASE_BUSSOLA = os.getenv("URI_DATABASE_BUSSOLA")
engine = create_engine(URI_DATABASE_BUSSOLA)

# Dicionário de mapeamento: {Nome_da_Tabela: "Nome_do_Arquivo.csv"}
# Ajuste os nomes dos arquivos .csv conforme aparecem na sua pasta docs/database
tabelas_mapeadas = {
    "criterios": "CRITERIOS.csv",
    "rais_estabelecimentos": "RAIS ESTABELECIMENTOS.csv",
    "top100_30": "TOP100_30.csv",
    "top100_15": "TOP100_15.csv",
    "situacional_2023": "SITUACIONAL_2023.csv",
    "salarios_e_visitas": "Salários e Visitas.csv",
    "situacional_2023_pivot_median": "SITUACIONAL_2023_PIVOT_MEDIAN.csv",
    "atividade_turistica": "atividade_turistica.csv",
    "pivot_situacional": "PIVOT_SITUACIONAL.csv",
    "ibge": "IBGE.csv",
    "destinations_2023": "DESTINATIONS_2023.csv",
    "timeline_full": "TIMELINE_FULL.csv",
    "qquadrado": "QQUADRADO.csv",
    "planilha1": "Planilha1.csv",
    "selo": "SELO.csv",
    "timeline_gd": "TIMELINE_GD.csv",
    "correlacao": "CORRELACAO.csv",
    "language": "LANGUAGE.csv",
    "pivot_top100c15": "PIVOT_TOP100C15.csv",
    "pivot_gd": "PIVOT_GD.csv",
    "pivot_top100c30": "PIVOT_TOP100C30.csv",
    "criterios_situacional": "CRITERIOS_SITUACIONAL.csv",
    "timeline_full_detail": "TIMELINE_FULL_DETAIL.csv",
    "situacional_2023_pivot": "SITUACIONAL_2023_PIVOT.csv",
    "remuneracao": "REMUNERACAO.csv",
    "rais_geral": "RAIS GERAL.csv",
    "dicionario": "dicionario_dados_agente.csv"
}

def importar_dados():
    if not URI_DATABASE_BUSSOLA:
        print("Erro: URI_DATABASE_BUSSOLA não encontrada nas variáveis de ambiente.")
        return

    print(f"Iniciando carga de dados no PostgreSQL...")

    for tabela, arquivo in tabelas_mapeadas.items():
        caminho_completo = os.path.join(PATH_CSV, arquivo)
        
        if os.path.exists(caminho_completo):
            try:
                # Carregando o CSV
                df = pd.read_csv(caminho_completo, encoding='latin-1', sep=None, engine='python')
                
                # Normalização de nomes de colunas 
                # Remove espaços e pontos que quebram queries SQL automáticas
                df.columns = [c.strip().replace(' ', '_').replace('.', '_').lower() for c in df.columns]
                
                # Enviando para o Postgres
                df.to_sql(tabela, engine, if_exists='replace', index=False)
                print(f"Tabela '{tabela}' importada com sucesso ({len(df)} linhas).")
                
            except Exception as e:
                print(f"Erro ao processar {arquivo}: {e}")
        else:
            print(f"Arquivo não encontrado: {caminho_completo}")

if __name__ == "__main__":
    importar_dados()


# PARA IMPORTAR O CSV DIRETO NO CONTAINER DO DOCKER É PRECISO PRIMEIRO SUBIR ELE COM O DOCKER COMPOSE
# E UTILIZAR O COMANDO NO TERMINAL EXTERNO: docker compose exec api uv run python -m scripts.import-bussola-db

# docker compose exec api uv run python scripts/import_bussola_db.py
