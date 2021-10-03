
class Point:
    name: str
    x: float
    y: float

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def get(self):
        return self.x, self.y


class Line:
    name: str
    x1: float
    y1: float
    x2: float
    y2: float

    def __init__(self, name, x1, y1, x2, y2):
        self.name = name
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get(self):
        return self.x1, self.x2, self.y1, self.y2
