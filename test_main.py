from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main_returns_not_found():
    response = client.get('/')
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}


def test_read_main_return_insira_novas_tarefas():
    response = client.get('/tarefas')
    assert response.status_code == 200
    assert response.json() == ["Insira novas tarefas"]

def test_delete_tarefa_vazio():
    response = client.delete('/tarefa/apagar/5')
    assert response.status_code == 404

def test_delete_tarefa_existente():
    response = client.post(
        "/tarefa/nova",
        json={"titulo": "Outra Tarefa", "desTarefa": "Descrição de Tarefa"},
    )
    response = client.delete('tarefa/apagar/0')
    assert response.status_code == 200

