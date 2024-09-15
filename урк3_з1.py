lesson = 'Урок 3, задание 1 \n'

print(lesson)
print('Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление')

def pos_arg(arg_1, arg_2):
    return arg_1 / arg_2
try:
    print(pos_arg(int(input("Введите целое число 1: ")), int(input("Введите целое число 2: "))))
except:
    print("Нельзя делить на ноль")
