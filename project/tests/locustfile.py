from locust import HttpUser, task


class Testing(HttpUser):
    @task(1)
    def test_id(self):
        self.client.get("/id/?=item_id=5")

    @task(2)
    def test_add_point(self):
        self.client.post("/add/point", json={"name": "Anya", "x": 0.1, "y": -0.32})

    @task(3)
    def test_add_line(self):
        self.client.post("/add/line", json={"name": "Anya", "x1": 0.4, "y1": 0.02, "x2": 8.3, "y2": -0.2})

    @task(4)
    def test_draw(self):
        self.client.get("/draw/?name=Anya")
