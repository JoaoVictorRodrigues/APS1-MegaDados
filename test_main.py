from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main_returns_not_found():
    response = client.get('/')
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}


def test_create_nova_tarefa():
    response = client.post(
        "/tarefa/nova",
        json={"titulo": "Outra Tarefa", "desTarefa": "Descrição de Tarefa"},
    )
    assert response.status_code == 200


def test_bad_create_nova_tarefa():
    response = client.post(
        "/tarefa/nova",
        json={"desTarefa": "Descrição de Tarefa"},
    )
    assert response.status_code == 422

def test_edit_inexistent_tarefa():
    response = client.put(
        "/tarefa/editar/10",
        json={"desTarefa": "Descrição de Tarefa"},
    )
    assert response.status_code == 404
