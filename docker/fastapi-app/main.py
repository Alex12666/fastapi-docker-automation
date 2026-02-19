from fastapi import FastAPI

# 1. Criamos a instância do servidor
app = FastAPI()

# 2. Criamos a rota "Hello World"
@app.get("/")
def read_root():
        return {"message": "Hello Alexandre! FastAPI está rodando."}

    # Para rodar, você vai precisar do uvicorn:
    # pip install fastapi uvicorn
    # uvicorn main:app --reload
