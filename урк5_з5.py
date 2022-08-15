lesson = 'Урок 5, задание 5 \n'

print(lesson)
print('Программа должна подсчитывать сумму чисел в файле и выводить её на экран.\n')

import random

myfile = open("z5.txt", "w", encoding="utf-8")
file_inp = random.sample(range(1, 10), 3)
myfile.write(" ".join(map(str, file_inp)))  # Позаимствовал строчку из разбора дз.
myfile.close()
print("Сумма чисел в файле:", sum(file_inp))
