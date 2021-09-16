import matplotlib.pyplot as plt

from fastapi import HTTPException


class Data_processing:

    flags = {
        'point': 'bo',
        'line': 'g-'
    }

    def __init__(self):
        self.d = dict()

    @staticmethod
    def check_name(name: str):
        if name == "":
            raise HTTPException(status_code=400, detail="Invalid name")

    def add_item(self, item, item_type):
        self.check_name(item.name)
        if item.name not in self.d:
            self.d[item.name] = dict()
        if item_type not in self.d[item.name]:
            self.d[item.name][item_type] = list()
        self.d[item.name][item_type].append(item.get())

    def draw_figure(self, name):
        plt.cla()
        for key, items in self.d[name].items():
            for i in items:
                plt.plot(i[:len(i) // 2], i[len(i) // 2:], self.flags[key])
        file_path = f'{name}.png'
        plt.savefig(file_path)
        return file_path

