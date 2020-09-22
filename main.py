from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class Tarefa(BaseModel):
    titulo: str
    desTarefa: str
    finalizado: bool = False


dbTarefas = {}

# Mostra todas as notas
@app.get("/tarefas")
async def read_all_tarefas(status: Optional[bool] = None):
    """ Mostra todas as tarefas. Use o status para filtrar as tarefas finalizadas/não finalizadas """
    if len(dbTarefas) == 0:
        return {"msg":"Insira novas tarefas"}
    elif status != None:
        dbfiltrado = {}
        for i in range(len(dbTarefas)):
            if dbTarefas[i].finalizado == status:
                dbfiltrado[i] = dbTarefas[i]
        return dbfiltrado
    else:
        return dbTarefas


# Mostra uma unica tarefa
@app.get("/tarefa/{tarefa_id}")
async def read_single_tarefa(tarefa_id: int, q: Optional[str] = None):
    """ Mostra um unica tarefa """
    selected = dbTarefas[tarefa_id]
    return selected

# Edita uma tarefa
@app.put("/tarefa/editar/{tarefa_id}")
async def update_tarefa(tarefa_id: int, tarefa: Tarefa):
    """ Edita uma tarefa já existente """
    try:
      if tarefa_id in dbTarefas:
          dbTarefas[tarefa_id] = tarefa
    except KeyError as exception:
        raise HTTPException(
            status_code = 404,
            detail='Task not found',
        ) from exception

    

# Cria uma tarefa
@app.post("/tarefa/nova")
async def create_tarefa(tarefa: Tarefa):
    """ Cria uma nova tarefa"""
    try:
        if len(dbTarefas) == 0:
            dbTarefas[0] = tarefa
        else:
            dbTarefas[max(dbTarefas.keys())+1] = tarefa
        return len(dbTarefas)
    except KeyError as exception:
        raise HTTPException(
            status_code = 422,
            detail='Unprocessable Entity',
        ) from exception

# Apaga uma tarefa
@app.delete("/tarefa/apagar/{tarefa_id}")
async def delete_tarefa(tarefa_id: int):
    """ Deleta uma tarefa existente"""
    del(dbTarefas[tarefa_id])
    return dbTarefas
