print('Урок 6, задание 3')
print('Реализовать базовый класс Worker. \n')

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return (self.name, self.surname)

    def get_total_income(self):
        return sum(self._income.values())

empl = Position("John", "Doe", "Lawyer", 5000, 1000)
print("Name: ", *empl.get_full_name())
print("Position: ", empl.position)
print("Salary: ", empl.get_total_income())

#Следуя описанию это задание +/- e всех должно быть одинаковое, у меня были проблемы с выводом данных, но я подкорректировал код с разбора дз.