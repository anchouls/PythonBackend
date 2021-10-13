import matplotlib.pyplot as plt

from fastapi import HTTPException
import requests


class Data_processing:

    flags = {
        'point': 'bo',
        'line': 'g-'
    }

    def __init__(self):
        self.d = dict()

    @staticmethod
    def check_name(user):
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        response = requests.post("http://127.0.0.1:8002/check_user",
                                 json={"name": user.name, "password": user.password})
        if response.status_code != 200:
            raise HTTPException(status_code=401, detail="Invalid name or password: "+response.text)

    def add_item(self, item, user, item_type):
        self.check_name(user)
        if user.name not in self.d:
            self.d[user.name] = dict()
        if item_type not in self.d[user.name]:
            self.d[user.name][item_type] = list()
        self.d[user.name][item_type].append(item.get())

    def draw_figure(self, user):
        self.check_name(user)
        plt.cla()
        for key, items in self.d[user.name].items():
            for i in items:
                plt.plot(i[:len(i) // 2], i[len(i) // 2:], self.flags[key])
        file_path = f'{user.name}.png'
        plt.savefig(file_path)
        return file_path

    def get_image_by_name(self, name):
        print(self.d)
        return self.d[name]

