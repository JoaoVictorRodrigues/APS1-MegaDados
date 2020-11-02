from pydantic import BaseModel

class Tarefa(BaseModel):
    titulo: str
    desTarefa: str
    finalizado: bool = False