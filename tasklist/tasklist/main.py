# pylint: disable=missing-module-docstring
from fastapi import FastAPI

from .routers import task

app = FastAPI()

app.include_router(
    task.router,
    prefix="/tarefa",
    responses={404: {"description": "Not found"}},
)
