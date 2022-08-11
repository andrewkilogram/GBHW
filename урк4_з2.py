lesson = 'Урок 4, задание 2 \n'

print(lesson)
print('Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.')

import random

mylist = random.sample(range(10, 100), 10)
#mylist = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
newlist = [n for i, n in zip(mylist, mylist[1:]) if n > i]
print("Исходный лист: ", mylist)
print("Результат:", newlist)

# Результат должен быть: [12, 44, 4, 10, 78, 123]
