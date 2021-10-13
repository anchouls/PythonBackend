from sqlalchemy import Column, Integer, String

from .database import Base


class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String)


class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String)
    id_image = Column(Integer)


class Line(Base):
    __tablename__ = "lines"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    id_image = Column(Integer)
    x1 = Column(Integer)
    x2 = Column(Integer)
    y1 = Column(Integer)
    y2 = Column(Integer)


class Point(Base):
    __tablename__ = "points"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    id_image = Column(Integer)
    x = Column(Integer)
    y = Column(Integer)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String, unique=True)
    pwd = Column(String)
