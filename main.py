from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def home():
    return {"Olá": "Mundo!"}

@app.get("/aleatorio/{limite}")
def numero_aleatorio(limite: int):
    num = random.randint(0, limite)
    return {"numero": num}