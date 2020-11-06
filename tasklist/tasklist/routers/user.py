import uuid

from typing import Dict

from fastapi import APIRouter, HTTPException, Depends

from ..database import DBSession, get_db
from ..models import User

router = APIRouter()


@router.get(
    '',
    summary='Reads user list',
    description='Reads the whole user list.',
    response_model=Dict[uuid.UUID, User],
)
async def read_users(db: DBSession = Depends(get_db)):
    return db.read_users()

@router.post(
    '',
    summary='Creates a new user',
    description='Creates a new task and returns its UUID.',
    response_model=uuid.UUID,
)
async def create_user(item: User, db: DBSession = Depends(get_db)):
    return db.create_user(item)

@router.get(
    '/{uuid_}',
    summary='Reads users',
    description='Reads users from UUID.',
    response_model=User,
)
async def read_user(uuid_: uuid.UUID, db: DBSession = Depends(get_db)):
    try:
        return db.read_user(uuid_)
    except KeyError as exception:
        raise HTTPException(
            status_code=404,
            detail='Task not found',
        ) from exception

@router.put(
    '/{uuid_}',
    summary='Replaces a task',
    description='Replaces a task identified by its UUID.',
)
async def replace_user(
        uuid_: uuid.UUID,
        item: User,
        db: DBSession = Depends(get_db),
 ):
    try:
        db.replace_user(uuid_, item)
    except KeyError as exception:
        raise HTTPException(
            status_code=404,
            detail='Task not found',
        ) from exception

@router.delete(
    '/{uuid_}',
    summary='Deletes task',
    description='Deletes a task identified by its UUID',
)
async def user(uuid_: uuid.UUID, db: DBSession = Depends(get_db)):
    try:
        db.remove_user(uuid_)
    except KeyError as exception:
        raise HTTPException(
            status_code=404,
            detail='Task not found',
        ) from exception
