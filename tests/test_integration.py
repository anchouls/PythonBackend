import pytest
from os import path

from fastapi import HTTPException

from app.main import Utils


class Point:
    name: str
    x: float
    y: float

    def get(self):
        return self.x, self.y


class Line:
    name: str
    x1: float
    y1: float
    x2: float
    y2: float

    def get(self):
        return self.x1, self.x2, self.y1, self.y2


def init_point(name, x, y):
    item = Point()
    item.name = name
    item.x = x
    item.y = y
    return item


def init_line(name, x1, y1, x2, y2):
    item = Line()
    item.name = name
    item.x1 = x1
    item.y1 = y1
    item.x2 = x2
    item.y2 = y2
    return item


def test_add_items_and_check_create_file():
    utils = Utils()
    utils.add_item(init_point('Anya', 0.1, -0.32), 'point')
    utils.add_item(init_point('Anya', 0.3, 0.2), 'point')
    utils.add_item(init_line('Anya', -0.01, -0.24, -1.1, 0.2), 'line')
    assert path.exists(utils.draw_figure('Anya'))


def test_correct_picture():
    utils = Utils()
    utils.add_item(init_point('A', 0.1, -0.32), 'point')
    utils.add_item(init_point('A', 0.3, 0.2), 'point')
    utils.add_item(init_line('A', -0.01, -0.24, -1.1, 0.2), 'line')
    path_picture = utils.draw_figure('A')
    with open(path_picture, 'rb') as f:
        with open('tests/Old.png', 'rb') as g:
            data1 = f.read(path.getsize(path_picture))
            data2 = g.read(path.getsize('tests/Old.png'))
            assert data1 == data2


@pytest.mark.xfail()
def test_if_check_name_failed_then_add_item_failed():
    utils = Utils()
    name = ''
    try:
        utils.check_name(name)
    except HTTPException:
        utils.add_item(init_point(name, 0.1, -0.32), 'point')








