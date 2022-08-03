lesson = 'Урок 2, задание 4 \n'

print(lesson)
print('Вывести каждое слово с новой строки')

spisok = input("Введите слова через пробел: ").split()

for i, spisok in enumerate(spisok):
    print(i + 1, "-", "%.10s" % (spisok))
