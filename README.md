# Assistente Bússola da Sustentabilidade

## Rodando em ambiente docker:

`docker compose up --build`

* Para visualizar a interface web do chat acesse: http://localhost:5173/
* Para entrar no Swagger do FastAPI do projeto acesse: http://127.0.0.1:8000/docs


## Configurações para run em ambiente de desenvolvimento:

Com o sistema rodando no container, deve-se fazer a importação dos arquivos necessários para popular o banco de dados local:

* A base de dados está no diretório **/docs/database**
* Para popular o banco de dados local com os arquivos da base de dados rode o script **import_bussola_db.py** com o comando:

`docker compose exec api uv run python scripts/import_bussola_db.py`

## Realizando perguntas testes

Para avaliar a funcionalidade do sistema, algumas perguntas testes foram realizadas. Com essas perguntas podemos analisar a **latência** do agente, sua precisão na chamada de **ferramentas** e continuidade de **contexto**.

Siga esse exemplo de fluxo de perguntas para manter o teste de contexto:

1. Liste as cidades que possuem selo de certificação gd 
2. Faça uma tabela com seus respectivos codigos ibge e as regiões dessas cidades
3. Faça uma comparação entre apodi e bombinhas 
4. Quais as cidades com selo de certiticação gd que possuem dados de avaliação?
5. Quais foram as avaliações da cidade bombinhas?
6. Compare com a cidade de orleans 

Algumas perguntas contém maior latência do que outras:


| Pergunta | Latência (s)
|:---:|:---:|
| 1 | 11 | 
| 2 | 30 | 
| 3 | 120 |
| 4 | 15 |
| 5 | 20 |
| 6 | 60 |

## Detalhes de funcionalidade [Construindo...]

O agente é capaz de guardar memórias de longo prazo como nomes e preferências de uso. Você pode fazer o teste com:

- "Meu nome é Jean"
- "Eu prefiro consultas da região Sul"

## Chat como widget em outro sistema 

Para testar o chat acoplado em outro sistema, desenvolvi um sistema React simples apenas para a implementação do chat em widget com o método `iframe`, onde é referenciado a URL do chat para o widget do sistema.

O sistema está no repositório [aqui](https://github.com/JeanMagnus/anchor-website-react).

Esse sistema não possui container docker configurado, é necessário possuir o react vite na máquina e então rode o sistema com esse comando:

`npm run dev -- --port 5174`