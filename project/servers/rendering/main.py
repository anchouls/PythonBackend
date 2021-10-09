from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles
from .data_processing import Data_processing
from project.servers.contracts import Point, Line, User

app = FastAPI()

data_processing = Data_processing()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/client", StaticFiles(directory="project/client"), name="client")


@app.get("/")
async def redirect():
    return RedirectResponse(url='/client/index.html')


@app.get("/id")
def get_id(item_id: int = 0):
    return {"id": item_id}


@app.post("/add/point")
async def add_point(item: Point, user: User):
    data_processing.add_item(item, user, 'point')


@app.post("/add/line")
async def add_line(item: Line, user: User):
    data_processing.add_item(item, user, 'line')


@app.get("/draw")
def draw(user: User):
    return FileResponse(data_processing.draw_figure(user))


@app.get("/get_image")
def get_image(name: str):
    return data_processing.get_image_by_name(name)


