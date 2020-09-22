
from fastapi import APIRouter, HTTPException, Depends
from typing import Optional
from api.database import DBSession, get_db
from api.models import Tarefa

router = APIRouter()


@router.get("")
async def read_all_tarefas(status: Optional[bool] = None, db: DBSession = Depends(get_db)):
    """ Mostra todas as tarefas. Use o status para filtrar as tarefas finalizadas/não finalizadas """
    return db.read_all_tarefas(status)


# Mostra uma unica tarefa
@router.get("/{tarefa_id}")
async def read_single_tarefa(tarefa_id: int, q: Optional[str] = None, db: DBSession = Depends(get_db)):
    """ Mostra um unica tarefa """
    return db.read_single_tarefa(tarefa_id)

# Edita uma tarefa


@router.put("/editar/{tarefa_id}")
async def update_tarefa(tarefa_id: int, tarefa: Tarefa, db: DBSession = Depends(get_db)):
    """ Edita uma tarefa já existente """
    try:
        if tarefa_id in db.dbTarefas:
            db.dbTarefas[tarefa_id] = tarefa
    except KeyError as exception:
        raise HTTPException(
            status_code=422,
            detail='Task not found',
        ) from exception


# Cria uma tarefa
@router.post("/nova")
async def create_tarefa(tarefa: Tarefa, db: DBSession = Depends(get_db)):
    """ Cria uma nova tarefa"""
    return db.create_tarefa(tarefa)

# Apaga uma tarefa


@router.delete("/apagar/{tarefa_id}")
async def delete_tarefa(tarefa_id: int, db: DBSession = Depends(get_db)):
    """ Deleta uma tarefa existente"""
    try:
        del(db.dbTarefas[tarefa_id])
        # return db.dbTarefas
    except KeyError as exception:
        raise HTTPException(
            status_code=404,
            detail='Task not found',
        ) from exception
