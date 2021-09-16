from pydantic import BaseModel


class Point(BaseModel):
    name: str
    x: float
    y: float

    def get(self):
        return self.x, self.y


class Line(BaseModel):
    name: str
    x1: float
    y1: float
    x2: float
    y2: float

    def get(self):
        return self.x1, self.x2, self.y1, self.y2

