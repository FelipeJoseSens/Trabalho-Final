# API de Venda de Ingressos para Eventos

Este projeto é uma API RESTful para listar eventos com ingressos à venda, desenvolvido como parte do trabalho final da disciplina de Cloud Computing.

## Tecnologias Utilizadas
- Python 3.9+
- FastAPI
- Uvicorn
- Pytest

## Configuração do Ambiente Local

1.  **Clone o repositório:**
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    cd [NOME_DA_PASTA_DO_PROJETO]
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

## Executando a API

Para iniciar o servidor localmente na porta 8000, execute:
```bash
uvicorn api.main:app --reload --port 8000


"Projeto Finalizado.".