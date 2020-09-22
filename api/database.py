class DBSession:
  dbTarefas = {}
  def __init__(self):
      self.tasks = DBSession.dbTarefas

def get_db():
  return DBSession()