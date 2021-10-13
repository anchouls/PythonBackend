import pytest

from project.servers.database import curd, db_models
from project.servers.database.database import SessionLocal, engine

db_models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_user():
    with SessionLocal() as db:
        curd.add_user(db, "anya", "password")
        assert curd.is_user(db, "anya").name == "anya"
        assert curd.is_user_pwd(db, "anya", "password").pwd == "password"


def test_image():
    with SessionLocal() as db:
        true_lines = [[1.9, 3.5, 0.4, 7.2], [9.3, 5.7, 3.2, 9.7]]
        true_points = [[6.7, 7.4], [0.1, 1.3]]
        ind = curd.add_image(db, "anya", ["image", "thesis"], true_lines, true_points)
        lines = curd.get_lines(db, ind)
        for line in lines:
            assert [line.x1, line.x2, line.y1, line.y2] in true_lines
        assert len(lines) == len(true_lines)
        points = curd.get_points(db, ind)
        for point in points:
            assert [point.x, point.y] in true_points
        assert len(points) == len(true_points)


def test_search_image():
    with SessionLocal() as db:
        ind1 = curd.add_image(db, "alex", ["vectors", "graph"], [[1.5, 4.5, 2.4, 7.2]], [[7.7, 5.4], [2.1, 1.4]])
        curd.add_image(db, "martin", ["science", "ml"], [[2.9, 3.65, 20.4, 73.2], [93.3, 52.7, 34.2, 9.47]],
                              [[0.7, 7.4]])
        ind3 = curd.add_image(db, "sasha", ["vectors", "ai"], [[9.3, 5.7, 3.2, 9.7]], [[0.1, 1.3]])
        id_images = curd.search_image(db, "vectors")
        true_id = [ind1, ind3]
        for i in id_images:
            assert i in true_id
        assert len(true_id) == len(id_images)

