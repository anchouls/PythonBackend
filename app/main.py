import matplotlib.pyplot as plt

from fastapi import FastAPI, HTTPException

from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles


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


class Utils:
    flags = {
        'point': 'bo',
        'line': 'g-'
    }

    def __init__(self):
        self.d = dict()

    @staticmethod
    def check_name(name: str):
        if name == "":
            raise HTTPException(status_code=400, detail="Invalid name")

    def add_item(self, item, item_type):
        self.check_name(item.name)
        if item.name not in self.d:
            self.d[item.name] = dict()
        if item_type not in self.d[item.name]:
            self.d[item.name][item_type] = list()
        self.d[item.name][item_type].append(item.get())

    def draw_figure(self, name):
        plt.cla()
        for key, items in self.d[name].items():
            for i in items:
                plt.plot(i[:len(i) // 2], i[len(i) // 2:], self.flags[key])
        file_path = f'{name}.png'
        plt.savefig(file_path)
        return file_path


app = FastAPI()

utils = Utils()

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


@app.get("/id")
def get_id(item_id: int = 0):
    return {"id": item_id}


@app.post("/add/point")
async def add_point(item: Point):
    utils.add_item(item, 'point')


@app.post("/add/line")
async def add_line(item: Line):
    utils.add_item(item, 'line')


@app.get("/draw")
def draw(name: str = ""):
    utils.check_name(name)
    return FileResponse(utils.draw_figure(name))


