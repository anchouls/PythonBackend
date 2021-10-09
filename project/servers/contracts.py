from pydantic import BaseModel


class Point(BaseModel):
    x: float
    y: float

    def get(self):
        return self.x, self.y


class Line(BaseModel):
    x1: float
    y1: float
    x2: float
    y2: float

    def get(self):
        return self.x1, self.x2, self.y1, self.y2


class User(BaseModel):
    name: str
    password: str
