print('Урок 8, задание 2')
print('Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. \n')

class MyError(Exception):
    def __init__(self, txt):
            self.txt = txt

def div(s_1, s_2):
    try:
        s_1, s_2 = int(s_1), int(s_2)
        if s_2 == 0:
            raise MyError("Нельзя делить на ноль.")
        return round(s_1 / s_2, 2)
    except MyError as my_error:
        return my_error

print(div(input("Введите делимое: "), input("Введите делитель: ")))