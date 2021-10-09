import pytest
from os import path

from fastapi import HTTPException

from project.servers.rendering import Data_processing
from project.servers.rendering.entity import Point, Line


def test_add_items_and_check_create_file():
    data_processing = Data_processing()
    data_processing.add_item(Point('Anya', 0.1, -0.32), 'point')
    data_processing.add_item(Point('Anya', 0.3, 0.2), 'point')
    data_processing.add_item(Line('Anya', -0.01, -0.24, -1.1, 0.2), 'line')
    assert path.exists(data_processing.draw_figure('Anya'))


def test_correct_picture():
    data_processing = Data_processing()
    data_processing.add_item(Point('A', 0.1, -0.32), 'point')
    data_processing.add_item(Point('A', 0.3, 0.2), 'point')
    data_processing.add_item(Line('A', -0.01, -0.24, -1.1, 0.2), 'line')
    path_picture = data_processing.draw_figure('A')
    with open(path_picture, 'rb') as f:
        with open('tests/Old.png', 'rb') as g:
            data1 = f.read(path.getsize(path_picture))
            data2 = g.read(path.getsize('tests/Old.png'))
            assert data1 == data2


@pytest.mark.xfail()
def test_if_check_name_failed_then_add_item_failed():
    data_processing = Data_processing()
    name = ''
    try:
        data_processing.check_name(name)
    except HTTPException:
        data_processing.add_item(Point(name, 0.1, -0.32), 'point')








