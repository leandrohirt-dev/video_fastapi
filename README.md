# Tutorial FastAPI

Este projeto é um exemplo simples de uma API construída com [FastAPI](https://fastapi.tiangolo.com/), criado para um tutorial no YouTube.

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/leandrohirt-dev/video_fastapi.git
cd video_fastapi
```

2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Execução

Para rodar o servidor de desenvolvimento:

```bash
fastapi dev main.py
```

O servidor iniciará em `http://127.0.0.1:8000`.

## Endpoints

- `GET /`: Retorna uma mensagem de boas-vindas.
- `GET /aleatorio/{limite}`: Retorna um número aleatório entre 0 e o limite especificado.
