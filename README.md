# Assistente Bússola da Sustentabilidade

## Rodando em ambiente docker:

`docker compose up --build`

* No navegador acesse: http://127.0.0.1:8000/docs


## Configurações para run em ambiente de desenvolvimento:

Com o sistema rodando no docker, deve-se fazer a importação dos arquivos necessários para popular o banco de dados local:

* A base de dados está no diretório **/docs/database**
* Para popular o banco de dados local com os arquivos da base de dados rode o script **import_bussola_db.py** com o comando:

`docker compose exec api uv run python scripts/import_bussola_db.py`

