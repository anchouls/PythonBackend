from typing import List
import requests
from project.servers.contracts import User

from fastapi import FastAPI, HTTPException

from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Image:
    def __init__(self, name, d, ind, tags):
        self.name = name
        self.d = d
        self.ind = ind
        self.tags = tags


images = list()


@app.post("/add_image")
def add_image(user: User, tags: List[str]):
    response = requests.post("http://127.0.0.1:8002/check_user", data={'user': {'name': user.name, 'password':  user.password}})
    if not response.json():
        raise HTTPException(status_code=401, detail="Invalid name or password")

    response2 = requests.get("http://127.0.0.1:8000/get_image/?name=" + user.name)
    d = response2.json()
    ind = len(images)
    images.append(Image(user, d, ind, tags))
    return ind


@app.get("/get_image")
async def get_image(item_id: int):
    return images[item_id]


@app.post("/search_image")
async def search_image(tags: List[str]):
    ans = list()
    for i in images:
        for t in tags:
            if t in i.tags:
                ans.append(i)
    return ans


