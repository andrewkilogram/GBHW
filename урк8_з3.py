print('Урок 8, задание 3')
print('Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. \n')

class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list = []

while True:
    inp_data = input("Введите число: ")
    if inp_data == "":
        break
    try:
        if inp_data.replace("-", "").replace(".", "").isdigit():
            my_list.append(float(inp_data))
        else:
            raise MyError("Введено не число")
    except MyError as my_error:
        print(my_error)
        continue

print(my_list)