from .models import Tarefa
from fastapi import FastAPI, HTTPException, Depends
class DBSession:
  dbTarefas = {}
  def __init__(self):
      self.dbTarefas = DBSession.dbTarefas

  def metodo_editar(self, tarefa_id: int, terefa: Tarefa):
    try:
      if tarefa_id in self.dbTarefas:
            self.dbTarefas[tarefa_id] = tarefa
    except KeyError as exception:
      raise HTTPException(
            status_code=422,
            detail='Task not found',
        ) from exception

  def metodo_delete(self, tarefa_id: int):
    try:
      del(self.dbTarefas[tarefa_id])
    except KeyError as exception:
        raise HTTPException(
            status_code=404,
            detail='Task not found',
        ) from exception

def get_db():
  return DBSession()