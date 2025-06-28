from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_read_status():
    """Testa a rota /status."""
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_get_eventos_disponiveis_sucesso():
    """Testa se a rota /eventos_disponiveis retorna status 200 e uma lista."""
    response = client.get("/eventos_disponiveis")
    assert response.status_code == 200
    # Verifica se o retorno é uma lista (JSON array)
    assert isinstance(response.json(), list)

def test_conteudo_dos_eventos():
    """Testa se a lista de eventos não está vazia e se o primeiro item tem as chaves esperadas."""
    response = client.get("/eventos_disponiveis")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    # Verifica as chaves do primeiro evento
    primeiro_evento = data[0]
    assert "id_evento" in primeiro_evento
    assert "nome_evento" in primeiro_evento
    assert "cidade" in primeiro_evento
    assert "preco_minimo_ingresso" in primeiro_evento