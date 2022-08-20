print('Урок 6, задание 5')
print('Реализовать класс Stationery. \n')

class Stationery:
    def __init__(self, title="Запуск отрисовки"):
        self.title = title

    def draw(self):
        print(self.title)

class Pen(Stationery):
    def draw(self):
        print("Рисуем", self.title)

class Pencil(Stationery):
    def draw(self):
        print("Рисуем", self.title)

class Handle(Stationery):
    def draw(self):
        print("Рисуем", self.title)

statationery = Stationery()
pen = Pen("Ручкой")
pencil = Pencil("Карандашом")
handle = Handle("Маркером")

stati_list = [statationery, pen, pencil, handle]
for i in stati_list:
    i.draw()