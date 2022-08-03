lesson = 'Урок 2, задание 2 \n'

print(lesson)
print('Для списка реализовать обмен значений соседних элементов')

#spisok_inp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Набор для проверки.
spisok = input("Введите элементы списка: ").split()

for i in range(0, len(spisok) - 1, 2):
    spisok[i], spisok[i + 1] = spisok[i + 1], spisok[i]

print(spisok)