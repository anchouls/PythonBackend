import pytest
from os import path

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


def test_check_name_not_fall():
    utils = Utils()
    utils.check_name('Alex')


@pytest.mark.xfail()
def test_check_name_fall():
    utils = Utils()
    utils.check_name('')


def test_check_name_not_fall_with_number_str():
    utils = Utils()
    utils.check_name('1')


def init_point(name, x, y):
    item = Point()
    item.name = name
    item.x = x
    item.y = y
    return item


def test_add_item_check_adding_point():
    utils = Utils()
    utils.add_item(init_point('Anya', 0.1, -0.32), 'point')
    assert len(utils.d) == 1
    assert len(utils.d['Anya']) == 1
    assert utils.d['Anya']['point'] == [(0.1, -0.32)]


def init_line(name, x1, y1, x2, y2):
    item = Line()
    item.name = name
    item.x1 = x1
    item.y1 = y1
    item.x2 = x2
    item.y2 = y2
    return item


def test_add_item_check_adding_line():
    utils = Utils()
    utils.add_item(init_line('Anya', 0.02, -0.3, -0.2, 0.99), 'line')
    assert len(utils.d) == 1
    assert len(utils.d['Anya']['line']) == 1
    assert utils.d['Anya']['line'] == [(0.02, -0.2, -0.3, 0.99)]


def test_add_item_adding_lines_and_points():
    utils = Utils()
    utils.add_item(init_point('Anya', 0.1, -0.32), 'point')
    utils.add_item(init_point('Anya', -0.2, 0.01), 'point')
    utils.add_item(init_line('Anya', 0.02, -0.3, -0.2, 0.99), 'line')
    utils.add_item(init_point('Anya', 0.76, 0.77), 'point')
    utils.add_item(init_line('Anya', -0.33, -0.5, 0.66, -0.09), 'line')
    utils.add_item(init_point('Alex', 0.01, -0.02), 'point')
    utils.add_item(init_line('Alex', 0.52, -0.63, -0.2, 0.9), 'line')
    utils.add_item(init_point('Alex', -0.12, 0.31), 'point')
    utils.add_item(init_point('Alex', 0.6, 0.7), 'point')
    utils.add_item(init_line('Alex', -0.3, -0.65, 0.6, -0.9), 'line')
    assert utils.d['Anya']['point'] == [(0.1, -0.32), (-0.2, 0.01), (0.76, 0.77)]
    assert utils.d['Anya']['line'] == [(0.02, -0.2, -0.3, 0.99), (-0.33, 0.66, -0.5, -0.09)]
    assert utils.d['Alex']['point'] == [(0.01, -0.02), (-0.12, 0.31), (0.6, 0.7)]
    assert utils.d['Alex']['line'] == [(0.52, -0.2, -0.63, 0.9), (-0.3, 0.6, -0.65, -0.9)]


def test_draw_figure_check_create_file():
    utils = Utils()
    utils.d['Anya'] = dict()
    utils.d['Anya']['point'] = [(0.1, -0.32), (-0.2, 0.01), (0.76, 0.77)]
    utils.d['Anya']['line'] = [(0.02, -0.2, -0.3, 0.99), (-0.33, 0.66, -0.5, -0.09)]
    assert path.exists(utils.draw_figure('Anya'))


def test_draw_figure_file_weight_increased():
    utils = Utils()
    utils.d['Anya'] = dict()
    utils.d['Anya']['point'] = [(0.1, -0.32), (-0.2, 0.01), (0.76, 0.77)]
    w1 = path.getsize(utils.draw_figure('Anya'))
    utils.d['Anya']['line'] = [(0.02, -0.2, -0.3, 0.99), (-0.33, 0.66, -0.5, -0.09)]
    w2 = path.getsize(utils.draw_figure('Anya'))
    assert w2 > w1


def test_draw_figure():
    utils = Utils()
    utils.d['Anya'] = dict()
    utils.d['Anya']['point'] = [(0.1, -0.32), (-0.2, 0.01), (0.76, 0.77)]
    w1 = path.getsize(utils.draw_figure('Anya'))
    utils.d['Alex'] = dict()
    utils.d['Alex']['point'] = [(0.01, -0.02), (-0.12, 0.31), (0.6, 0.7)]
    w2 = path.getsize(utils.draw_figure('Anya'))
    assert w2 == w1




