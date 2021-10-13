from typing import List

from sqlalchemy.orm import Session
from . import db_models
from ..rendering.entity import Line, Point


def add_user(db: Session, name: str, password: str):
    db_user = db_models.User(name=name, pwd=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)


def is_user_pwd(db: Session, name: str, password: str):
    return db.query(db_models.User).filter(db_models.User.name == name, db_models.User.pwd == password).first()


def is_user(db: Session, name: str):
    return db.query(db_models.User).filter(db_models.User.name == name).first()


def add_image(db: Session, name: str, tags: List[str], lines: List[List[float]], points: List[List[float]]):
    db_image = db_models.Image(name=name)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    id_image = db_image.id
    for t in tags:
        db_tag = db_models.Tag(name=t, id_image=id_image)
        db.add(db_tag)
    for line in lines:
        print(line)
        db_line = db_models.Line(id_image=id_image, x1=line[0], x2=line[1], y1=line[2], y2=line[3])
        db.add(db_line)
    for p in points:
        db_point = db_models.Point(id_image=id_image, x=p[0], y=p[1])
        db.add(db_point)
    db.commit()
    return id_image


def get_lines(db: Session, id_image: int):
    return db.query(db_models.Line).filter(db_models.Line.id_image == id_image).all()


def get_points(db: Session, id_image: int):
    return db.query(db_models.Point).filter(db_models.Point.id_image == id_image).all()


def search_image(db: Session, tag: str):
    images = db.query(db_models.Tag).filter(db_models.Tag.name == tag).all()
    return [i.id_image for i in images]
