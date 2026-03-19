
# Instalando uv no docker (usei a documentação https://docs.astral.sh/uv/guides/integration/docker/#available-images)
FROM python:3.12-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/


# Define o diretório de trabalho
WORKDIR /app

# Impede que o Python gere arquivos .pyc e permite logs em tempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instala as dependências primeiro para aproveitar o cache do Docker
# Copia apenas os arquivos de lock e config do uv
COPY pyproject.toml uv.lock /app/

# Instala as dependências do projeto (sem instalar o projeto em si ainda)
RUN uv sync --locked

# Agora copia o restante do código
COPY . /app/

# Comando para rodar a aplicação usando o uv para garantir o ambiente virtual correto
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]