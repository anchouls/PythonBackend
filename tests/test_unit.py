import pytest
from os import path

from app.data_processing import Data_processing
from app.entity import Point, Line


def test_check_name_not_fall():
    data_processing = Data_processing()
    data_processing.check_name('Alex')


@pytest.mark.xfail()
def test_check_name_fall():
    data_processing = Data_processing()
    data_processing.check_name('')


def test_check_name_not_fall_with_number_str():
    data_processing = Data_processing()
    data_processing.check_name('1')


def test_add_item_check_adding_point():
    data_processing = Data_processing()
    data_processing.add_item(Point('Anya', 0.1, -0.32), 'point')
    assert len(data_processing.d) == 1
    assert len(data_processing.d['Anya']) == 1
    assert data_processing.d['Anya']['point'] == [(0.1, -0.32)]


def test_add_item_check_adding_line():
    data_processing = Data_processing()
    data_processing.add_item(Line('Anya', 0.02, -0.3, -0.2, 0.99), 'line')
    assert len(data_processing.d) == 1
    assert len(data_processing.d['Anya']['line']) == 1
    assert data_processing.d['Anya']['line'] == [(0.02, -0.2, -0.3, 0.99)]


def test_add_item_adding_lines_and_points():
    data_processing = Data_processing()
    data_processing.add_item(Point('Anya', 0.1, -0.32), 'point')
    data_processing.add_item(Point('Anya', -0.2, 0.01), 'point')
    data_processing.add_item(Line('Anya', 0.02, -0.3, -0.2, 0.99), 'line')
    data_processing.add_item(Point('Anya', 0.76, 0.77), 'point')
    data_processing.add_item(Line('Anya', -0.33, -0.5, 0.66, -0.09), 'line')
    data_processing.add_item(Point('Alex', 0.01, -0.02), 'point')
    data_processing.add_item(Line('Alex', 0.52, -0.63, -0.2, 0.9), 'line')
    data_processing.add_item(Point('Alex', -0.12, 0.31), 'point')
    data_processing.add_item(Point('Alex', 0.6, 0.7), 'point')
    data_processing.add_item(Line('Alex', -0.3, -0.65, 0.6, -0.9), 'line')
    assert data_processing.d['Anya']['point'] == [(0.1, -0.32), (-0.2, 0.01), (0.76, 0.77)]
    assert data_processing.d['Anya']['line'] == [(0.02, -0.2, -0.3, 0.99), (-0.33, 0.66, -0.5, -0.09)]
    assert data_processing.d['Alex']['point'] == [(0.01, -0.02), (-0.12, 0.31), (0.6, 0.7)]
    assert data_processing.d['Alex']['line'] == [(0.52, -0.2, -0.63, 0.9), (-0.3, 0.6, -0.65, -0.9)]


def test_draw_figure_check_create_file():
    data_processing = Data_processing()
    data_processing.d['Anya'] = dict()
    data_processing.d['Anya']['point'] = [(0.1, -0.32), (-0.2, 0.01), (0.76, 0.77)]
    data_processing.d['Anya']['line'] = [(0.02, -0.2, -0.3, 0.99), (-0.33, 0.66, -0.5, -0.09)]
    assert path.exists(data_processing.draw_figure('Anya'))


def test_draw_figure_file_weight_increased():
    data_processing = Data_processing()
    data_processing.d['Anya'] = dict()
    data_processing.d['Anya']['point'] = [(0.1, -0.32), (-0.2, 0.01), (0.76, 0.77)]
    w1 = path.getsize(data_processing.draw_figure('Anya'))
    data_processing.d['Anya']['line'] = [(0.02, -0.2, -0.3, 0.99), (-0.33, 0.66, -0.5, -0.09)]
    w2 = path.getsize(data_processing.draw_figure('Anya'))
    assert w2 > w1


def test_draw_figure():
    data_processing = Data_processing()
    data_processing.d['Anya'] = dict()
    data_processing.d['Anya']['point'] = [(0.1, -0.32), (-0.2, 0.01), (0.76, 0.77)]
    w1 = path.getsize(data_processing.draw_figure('Anya'))
    data_processing.d['Alex'] = dict()
    data_processing.d['Alex']['point'] = [(0.01, -0.02), (-0.12, 0.31), (0.6, 0.7)]
    w2 = path.getsize(data_processing.draw_figure('Anya'))
    assert w2 == w1




