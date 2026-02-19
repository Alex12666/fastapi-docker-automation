cat <<EOF > README.md
# FastAPI Docker Automation 🐳

Este projeto faz parte dos meus estudos de **DevOps**. Ele consiste em uma API assíncrona desenvolvida com **FastAPI**, totalmente containerizada com **Docker** e preparada para deploy automatizado em ambiente Linux (WSL2).

## 🚀 Tecnologias
* **Python 3.11-slim**: Imagem leve e otimizada para produção.
* **FastAPI**: Framework moderno de alta performance.
* **Docker**: Containerização para garantir que o código rode em qualquer lugar.
* **Bash**: Scripts de automação para build e deploy.

## 🛠️ Como Executar

### Pré-requisitos
* Docker instalado e rodando.
* WSL2 configurado (se estiver no Windows).

### Passo 1: Build da Imagem
\`\`\`bash
docker build -t fast-app .
\`\`\`

### Passo 2: Rodar o Container
\`\`\`bash
docker run -d -p 8000:8000 --name meu-fastapi fast-app
\`\`\`

Agora, acesse a API em: **http://localhost:8000**

## 📂 Estrutura do Repositório
* \`main.py\`: Código fonte da API.
* \`Dockerfile\`: Configuração da imagem Docker.
* \`requirements.txt\`: Lista de dependências Python.
* \`deploy.sh\`: Script de automação para facilitar o deploy.

---
Desenvolvido por **Alexandre Maia Jesus** 🚀
EOF
