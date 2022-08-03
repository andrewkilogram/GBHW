lesson =  'Урок 2, задание 3 \n'

print(lesson)
print('Сообщить, к какому времени года относится введеный месяц "LIST"')

mon = int(input("Введите месяц (целое число 1-12): "))
seasons = ["Это месяц весны", "Это месяц лета", "Это месяц осени", "Это месяц зимы"]

if 3 == mon or 4 == mon or 5 == mon:
    print(seasons[0])
else:
    if 6 == mon or 7 == mon or 8 == mon:
        print(seasons[1])
    else:
        if 9 == mon or 10 == mon or 11 == mon:
            print(seasons[2])
        else:
            if 12 == mon or 1 == mon or 2 == mon:
                print(seasons[3])

#Не смог придумать как сделать задание через список, придумал только такой вариант с if