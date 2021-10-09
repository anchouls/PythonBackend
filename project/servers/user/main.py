from fastapi import FastAPI
from project.servers.contracts import User

from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

users = dict()


@app.post("/check_user")
async def check_user(item: User):
    if item.name in users:
        if users[item.name] == item.password:
            return True
        else:
            return False
    else:
        return False


@app.post("/add_user")
async def add_user(item: User):
    if item.name in users:
        return False
    else:
        users[item.name] = item.password
        return True
