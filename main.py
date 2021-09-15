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


class Point(BaseModel):
    name: str
    x: float
    y: float

    def get(self):
        return self.x, self.y


class Line(BaseModel):
    name: str
    x1: float
    y1: float
    x2: float
    y2: float

    def get(self):
        return self.x1, self.x2, self.y1, self.y2


d = dict()
flags = {
    'point': 'bo',
    'line': 'g-'
}


def check_name(name: str):
    if name == "":
        raise HTTPException(status_code=400, detail="Invalid name")


def add_item(item, item_type):
    check_name(item.name)
    if item.name not in d:
        d[item.name] = dict()
    if item_type not in d[item.name]:
        d[item.name][item_type] = list()
    d[item.name][item_type].append(item.get())


def draw_figure(name):
    plt.cla()
    for key, items in d[name].items():
        for i in items:
            plt.plot(i[:len(i) // 2], i[len(i) // 2:], flags[key])
    file_path = f'{name}.png'
    plt.savefig(file_path)
    return file_path


@app.get("/")
async def redirect():
    return RedirectResponse(url='/client/index.html')


@app.get("/id")
def get_id(item_id: int = 0):
    return {"id": item_id}


@app.post("/add/point")
async def add_point(item: Point):
    add_item(item, 'point')


@app.post("/add/line")
async def add_line(item: Line):
    add_item(item, 'line')


@app.get("/draw")
def draw(name: str = ""):
    check_name(name)
    return FileResponse(draw_figure(name))


