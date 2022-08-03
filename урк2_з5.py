lesson = 'Урок 2, задание 2 \n'

print(lesson)
print('Реализовать структуру «Рейтинг»')

# - - - Это решение запрещено женевской конвенцией.
# while True:
#     spisok.append(int(input("Введите целое натуральное число: ")))
#     spisok.sort(reverse=True)
#     print(spisok)

init_spisok = [10, 8, 6, 4, 2]

while True:

    spisok = init_spisok
    spisok_int = int(input("Введите целое натуральное число: "))

    for x in spisok:
        if x == spisok_int:
            xi = spisok.index(x)  # Выясняем индекс элемента Х равного введённому значению
            spisok.insert(xi + 1, spisok_int)  # Вставляем введенное значение за равным элементом списка
            print(spisok)
            break
        else:
            if x == spisok_int < x + 1:
                xaddeq = spisok.index(x)
                spisok.insert(xaddeq + 1, spisok_int)
                print(spisok)
                break
            else:
                if x <= spisok_int:
                    xaddmo = spisok.index(x)
                    spisok.insert(xaddmo, spisok_int)
                    print(spisok)
                    break
                else:
                    if spisok_int < min(spisok):
                        xaddle = spisok.index(min(spisok))
                        spisok.insert(xaddle + 1, spisok_int)
                        print(spisok)
                        break

# Знаю что выполнение задачи через циклы это дурной тон и вообще так нельзя, но по другому я пока не умею.
