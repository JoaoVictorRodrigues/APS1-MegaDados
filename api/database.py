from api.models import Tarefa
from fastapi import APIRouter, HTTPException, Depends

class DBSession:
    dbTarefas = {}

    def __init__(self):
        self.dbTarefas = DBSession.dbTarefas

    def read_all_tarefas(self, status: bool):
        if len(self.dbTarefas) == 0:
            return {"msg": "Insira novas tarefas"}
        elif status != None:
            dbfiltrado = {}
            for i in range(len(self.dbTarefas)):
                if self.dbTarefas[i].finalizado == status:
                    dbfiltrado[i] = self.dbTarefas[i]
            return dbfiltrado
        else:
            return self.dbTarefas

    def read_single_tarefa(self, tarefa_id: int, q: str):
        selected = self.dbTarefas[tarefa_id]
        return selected

    def create_tarefa(self, tarefa: Tarefa):
        try:
            if len(self.dbTarefas) == 0:
                self.dbTarefas[0] = tarefa
            else:
                self.dbTarefas[max(self.dbTarefas.keys())+1] = tarefa
            return len(self.dbTarefas)
        except KeyError as exception:
            raise HTTPException(
                status_code=422,
                detail='Unprocessable Entity',
            ) from exception

def get_db():
    return DBSession()
