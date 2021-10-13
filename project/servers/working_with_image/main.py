from typing import List
import requests
from project.servers.contracts import User

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from starlette.middleware.cors import CORSMiddleware

from ..database import db_models, curd
from ..database.database import SessionLocal, engine
import matplotlib.pyplot as plt
from fastapi.responses import FileResponse


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db_models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/add_image")
def add_image(user: User, tags: List[str], db: Session = Depends(get_db)):
    response = requests.post("http://127.0.0.1:8002/check_user", data={'user': {'name': user.name, 'password':  user.password}})
    if not response.json():
        raise HTTPException(status_code=401, detail="Invalid name or password")

    response2 = requests.get("http://127.0.0.1:8000/get_image/?name=" + user.name)
    print(response2.text)
    d = response2.json()
    return curd.add_image(db, user.name, tags, d.get("line", []), d.get("point", []))


@app.get("/get_image")
async def get_image(item_id: int, db: Session = Depends(get_db)):
    points = curd.get_points(db, item_id)
    lines = curd.get_lines(db, item_id)
    plt.cla()
    for p in points:
        plt.plot(p.x, p.y, 'bo')
    for l in lines:
        plt.plot([l.x1, l.x2], [l.y1, l.y2], 'g-')
    file_path = f'{item_id}.png'
    plt.savefig(file_path)
    return FileResponse(file_path)


@app.post("/search_image")
async def search_image(tags: List[str], db: Session = Depends(get_db)):
    ans = list()
    for t in tags:
        ans += curd.search_image(db, t)
    return list(set(ans))


