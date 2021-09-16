from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles
from app.data_processing import Data_processing
from app.contracts import Point, Line

app = FastAPI()

data_processing = Data_processing()

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
    data_processing.add_item(item, 'point')


@app.post("/add/line")
async def add_line(item: Line):
    data_processing.add_item(item, 'line')


@app.get("/draw")
def draw(name: str = ""):
    data_processing.check_name(name)
    return FileResponse(data_processing.draw_figure(name))


