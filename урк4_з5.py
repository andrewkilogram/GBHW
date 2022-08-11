lesson = 'Урок 4, задание 1 \n'

print(lesson)
print('Реализовать формирование списка')

from functools import reduce

def my_func(n1, n2):
    return n1 * n2
print(reduce(my_func, list(range(100, 1001, 2))))