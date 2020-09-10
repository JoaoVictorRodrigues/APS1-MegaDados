from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


db = {}

@app.get("/")
async def read_root():
    return db


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    selected = db[item_id]
    return selected


@app.put("/items/{item_id}")
async def update_item(item_id: int,item: Item):
    db[item_id] = item
    return db


@app.post("/items/{item_id}")
async def create_item(item_id: int,item: Item):
    db[item_id+1]=(item)
    return len(db)


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    del(db[item_id])
    return db