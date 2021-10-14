from sqlalchemy import Column, Integer, String, Float

from .database import Base


class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String(25))


class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String(25))
    id_image = Column(Integer)


class Line(Base):
    __tablename__ = "lines"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    id_image = Column(Integer)
    x1 = Column(Float)
    x2 = Column(Float)
    y1 = Column(Float)
    y2 = Column(Float)


class Point(Base):
    __tablename__ = "points"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    id_image = Column(Integer)
    x = Column(Float)
    y = Column(Float)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String(25), unique=True)
    pwd = Column(String(32))
