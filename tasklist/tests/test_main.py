from fastapi.testclient import TestClient
from ..tasklist.main import app

client = TestClient(app)


def test_read_main_returns_not_found():
    response = client.get('/')
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}


def test_read_empty_task_list():
    response = client.get('/tarefa')
    assert response.status_code == 200
    assert response.json() == {"msg": "Insira novas tarefas"}


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


def test_delete_tarefa_vazio():
    response = client.delete('/tarefa/apagar/5')
    assert response.status_code == 404
    assert response.json() == {'detail': 'Task not found'}


def test_delete_tarefa_existente():
    response = client.post(
        "/tarefa/nova",
        json={"titulo": "Outra Tarefa", "desTarefa": "Descrição de Tarefa"},
    )
    response = client.delete('tarefa/apagar/0')
    assert response.status_code == 200


def test_edit_inexistent_tarefa():
    response = client.put(
        "/tarefa/editar/10",
        json={"desTarefa": "Descrição de Tarefa"},
    )
    assert response.status_code == 422


def test_edit_put():
    response = client.post(
        "/tarefa/nova",
        json={"titulo": "Outra Tarefa", "desTarefa": "Descrição de Tarefa"},
    )
    response = client.put(
        'tarefa/editar/0',
        json={"titulo": "Tarefa Editada",
              "desTarefa": "Descrição de Tarefa", "finalizado": True},
    )
    assert response.status_code == 200
