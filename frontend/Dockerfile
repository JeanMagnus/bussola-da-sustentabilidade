# Usando a imagem Node.js (Alpine é menor)
FROM node:20-alpine

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de dependência
COPY package*.json ./

# Instala as dependências
RUN npm install

# Copia o restante do código
COPY . .

# Expõe a porta que o Vite usa
EXPOSE 5173

# Executa o Vite com --host para permitir acesso externo
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]