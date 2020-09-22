from api.routers import task

from fastapi import FastAPI

app = FastAPI()

app.include_router(
    task.router,
    prefix="/tarefa",
    responses={404: {"description": "Not found"}},
)
