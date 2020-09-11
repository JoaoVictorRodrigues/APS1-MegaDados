from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Tarefa(BaseModel):
    id: int
    desTarefa: str
    finalizado: bool

dbTarefas = {}

# Mostra todas as notas
@app.get("/tarefas/")
async def read_root():
    if len(dbTarefas) == 0:
        return {"Insira novas tarefas"}
    else:
        return dbTarefas

# Mostra uma unica tarefa
@app.get("/tarefa/{tarefa_id}")
async def read_tarefa(tarefa_id: int, q: Optional[str] = None):
    selected = dbTarefas[tarefa_id]
    return selected

@app.get("/tarefa/finalisada")
async def 
# # Mostra uma unica tarefa
# @app.get("/tarefa/teste")
# async def filter_tarefa():
#     fiil = dbTarefas[0]
#     return fiil


# Edita uma tarefa
@app.put("/tarefa/editar/{tarefa_id}")
async def update_tarefa(tarefa_id: int,tarefa: Tarefa):

    if tarefa_id in dbTarefas:
        dbTarefas[tarefa_id]= tarefa
    else:
        return{"Tarefa não encontrada"}
    return dbTarefas

#Cria uma tarefa
@app.post("/tarefa/nova")
async def create_tarefa(tarefa: Tarefa):
    if len(dbTarefas) == 0:
        dbTarefas[0]=tarefa
    elif len(dbTarefas) in dbTarefas:
        dbTarefas[len(dbTarefas)+1] = tarefa
    else:
        dbTarefas[len(dbTarefas)] = tarefa
    return len(dbTarefas)

# Apaga uma tarefa
@app.delete("/tarefa/apagar/{tarefa_id}")
def delete_tarefa(tarefa_id: int):
    del(dbTarefas[tarefa_id])
    return dbTarefas