from abc import ABC, abstractmethod

print('Урок 7, задание 2')
print('Реализовать проект расчёта суммарного расхода ткани на производство одежды. \n')

class Clothes(ABC):
    result = 0

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        Clothes.result += self.consumption + other.consumption
        return Costume(0)

    def __str__(self):
        res = Clothes.result
        Clothes.result = 0
        return f"{res}"

class Coat(Clothes):
    @property
    def consumption(self):
        return round(self.param / 6.5) + 0.5

class Costume(Clothes):
    @property
    def consumption(self):
        return round((2 * self.param + 0.3) / 100)

coat = Coat(48)
costume = Costume(176)
print(coat + costume)