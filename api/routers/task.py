
from fastapi import APIRouter, HTTPException, Depends
from typing import Optional
from ..database import DBSession, get_db
from ..models import Tarefa


router = APIRouter()

@router.get("")
async def read_all_tarefas(status: Optional[bool] = None, db: DBSession = Depends(get_db)):
    """ Mostra todas as tarefas. Use o status para filtrar as tarefas finalizadas/não finalizadas """
    if len(db.dbTarefas) == 0:
        return {"msg": "Insira novas tarefas"}
    elif status != None:
        dbfiltrado = {}
        for i in range(len(db.dbTarefas)):
            if db.dbTarefas[i].finalizado == status:
                dbfiltrado[i] = db.dbTarefas[i]
        return dbfiltrado
    else:
        return db.dbTarefas


# Mostra uma unica tarefa
@router.get("/{tarefa_id}")
async def read_single_tarefa(tarefa_id: int, q: Optional[str] = None, db: DBSession = Depends(get_db)):
    """ Mostra um unica tarefa """
    selected = db.dbTarefas[tarefa_id]
    return selected

# Edita uma tarefa


@router.put("/editar/{tarefa_id}")
async def update_tarefa(tarefa_id: int, tarefa: Tarefa, db: DBSession = Depends(get_db)):
    """ Edita uma tarefa já existente """
    DBSession.metodo_editar(tarefa_id, tarefa)


# Cria uma tarefa
@router.post("/nova")
async def create_tarefa(tarefa: Tarefa, db: DBSession = Depends(get_db)):
    """ Cria uma nova tarefa"""
    try:
        if len(db.dbTarefas) == 0:
            db.dbTarefas[0] = tarefa
        else:
            db.dbTarefas[max(db.dbTarefas.keys())+1] = tarefa
        return len(db.dbTarefas)
    except KeyError as exception:
        raise HTTPException(
            status_code=422,
            detail='Unprocessable Entity',
        ) from exception

# Apaga uma tarefa


@router.delete("/apagar/{tarefa_id}")
async def delete_tarefa(tarefa_id: int, db: DBSession = Depends(get_db)):
    """ Deleta uma tarefa existente"""
    DBSession.metodo_delete(tarefa_id)
