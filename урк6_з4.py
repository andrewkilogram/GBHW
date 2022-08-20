print('Урок 6, задание 4')
print('Реализуйте базовый класс Car. \n')

from random import choice
class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return self.name, self.color, "Начал движение"

    def stop(self):
        return self.name, self.color,  "Стоит на месте"

    def turn(self):
        self.directions = ["На лево", "На право", "Назад", "Прямо"]
        return self.name, self.color, "Поехал", choice(self.directions)

    def show_speed(self):
        return self.name, self.color, "Скорость автомобиля", self.speed

class TownCar(Car):
    def show_speed(self):
        return self.name, self.color, "Едет по городу с превышением!" if self.speed > 60 else "Едет по городу со скоростью:", self.speed

class SportCar(Car):
    def show_speed(self):
        return self.name, self.color, "Едет по городу со скоростью:", self.speed

class WorkCar(Car):
    def show_speed(self):
        return self.name, self.color, self.stop() if self.speed == 0 else "Едет по городу со скоростью:", self.speed

class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, is_police=True)
#Не понял почему у полицейской машины именно такая конструкция.

town_car = TownCar("Седан", "Белый", 61)
sport_car = SportCar("Купе", "Красный", 150)
work_car = WorkCar("Фура", "Серый", 0)
police_car = PoliceCar("Купе", "Полицейская ливрея", 120)

car_list = [town_car, sport_car, work_car, police_car]
for i in car_list:
    i.go()
    print(i.show_speed())
    i.turn()
    print(i.turn())
    i.stop()
    print(i.stop())