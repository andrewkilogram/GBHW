lesson = 'Урок 3, задание 3 \n'

print(lesson)
print('Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.')

def max_sum(arg_1, arg_2, arg_3):

#           Вариант 1
#     arg_1 = 15
#     arg_2 = 14
#     arg_3 = 16
#     arg_12 = arg_1 + arg_2
#     arg_23 = arg_2 + arg_3
#     arg_13 = arg_1 + arg_3
#     arg_max = max(arg_12, arg_23, arg_13)
#     return arg_max
# print(max_sum())

#           Вариант 2
    args = arg_1, arg_2, arg_3
    print(sum(args) - min(args))
max_sum(10, 20, 30)