from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from project.servers.contracts import User

from starlette.middleware.cors import CORSMiddleware

from ..database import db_models, curd
from ..database.database import SessionLocal, engine

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


@app.post("/check_user")
def check_user(item: User, db: Session = Depends(get_db)):
    if curd.is_user_pwd(db, item.name, item.password):
        return True
    else:
        return False


@app.post("/add_user")
async def add_user(item: User, db: Session = Depends(get_db)):
    if curd.is_user(db, item.name):
        return False
    else:
        curd.add_user(db, item.name, item.password)
        return True
