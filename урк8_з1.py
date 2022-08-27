print('Урок 8, задание 1')
print('Реализовать класс «Дата», \n')

class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def extr(cls, data):
        return f'День {int(data[0])}, Месяц {int(data[1])}, Год {int(data[2])}'

    @staticmethod
    def valid(data):
        if not int(data[0]) in range(1, 32) or not int(data[1]) in range(1, 13) or int(data[2]) > 99:
            return 'Дата введена неверно.'

    def data_func(self):
        result_1 = Data.extr(self.data.split('-'))
        result_2 = Data.valid(self.data.split('-'))
        return result_2 if result_2 else f'Преобразование типа в число\n{result_1}'

user_data = input('Введите дату в формате дд-мм-гг: ')
mc = Data(user_data)
print(mc.data_func())
