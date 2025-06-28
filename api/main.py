import json
from fastapi import FastAPI, HTTPException
from pathlib import Path

app = FastAPI()

# Caminho para o arquivo JSON de eventos
EVENTOS_FILE = Path(__file__).parent / "eventos.json"

def carregar_eventos():
    """Carrega os eventos do arquivo JSON."""
    if not EVENTOS_FILE.is_file():
        return []
    with open(EVENTOS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

@app.get("/status")
def read_status():
    """Verificação de funcionamento da API."""
    return {"status": "ok"}

@app.get("/eventos_disponiveis")
def get_eventos_disponiveis():
    """Retorna a lista de eventos com ingressos à venda."""
    eventos = carregar_eventos()
    if not eventos:
        raise HTTPException(status_code=404, detail="Nenhum evento encontrado")
    return eventos