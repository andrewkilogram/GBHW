lesson = 'Урок 4, задание 3 \n'

print(lesson)
print('Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21')

newlist = [n for n in range(20, 241) if n % 21 == 0 or n % 20 == 0]
print(newlist)
