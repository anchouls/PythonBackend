import math

from fastapi import FastAPI, HTTPException

from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/")
def read_item(item_id: int = 0):
    return {"id": item_id}


class ItemIn(BaseModel):
    name: str
    x: float
    y: float


@app.post("/items/")
async def create_item(item: ItemIn):
    if item.x == 0 and item.y == 0:
        raise HTTPException(status_code=400, detail="Invalid request")
    return math.sqrt(item.x * item.x + item.y * item.y)


@app.post("/")
async def create_item(item: int = 0):
    return {"id": item}
