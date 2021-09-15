import math
import matplotlib.pyplot as plt

from fastapi import FastAPI, HTTPException

from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/client", StaticFiles(directory="client"), name="client")


@app.get("/")
async def redirect():
    return RedirectResponse(url='/client/index.html')


@app.get("/items/")
def read_item(item_id: int = 0):
    return {"id": item_id}


class ItemIn(BaseModel):
    name: str
    x: float
    y: float


d = dict()


@app.post("/items/")
async def create_item(item: ItemIn):
    if item.x == 0 and item.y == 0:
        raise HTTPException(status_code=400, detail="Invalid request")
    if item.name in d:
        d[item.name].append((item.x, item.y))
    else:
        d[item.name] = [(item.x, item.y)]
    return math.sqrt(item.x ** 2 + item.y ** 2)


@app.get("/draw/{name}")
def draw(name: str):
    plt.cla()
    for (x, y) in d[name]:
        plt.plot(x, y, 'bo')
    file_path = f'{name}.png'
    plt.savefig(file_path)
    return FileResponse(file_path)

