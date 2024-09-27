lesson = 'Урок 5, задание 3 \n'

print(lesson)
print('Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.\n')

#myfile = open("text_3.txt", "r")

with open("text_3.txt", "r", encoding="utf-8") as f:
    print("Сотрудники с доходом менее 20000:")
    for line in f:
        linelist = line.split() #Разбиваем строки на столбцы
        sal = int(float(linelist[1])) #Берем второй столбец с зарплатой
        minsal = sal <= 20000 #Сортируем
        if minsal == True:
            print(linelist[0], "-", linelist[1]) #Выводим после проверки
        continue
with open("text_3.txt", "r", encoding="utf-8") as f:
    sallist = []
    for line in f:
        linelist = line.split() #Разбиваем строки на столбцы
        sal = int(float(linelist[1])) #Берем второй столбец с зарплатой
        sallist.append(sal) #Скидываем значения в список
        full_sal = sum(sallist) #Суммируем значения списка
        sum_lines = len(sallist) #Считаем сколько сотрудников
    print("Средняя величина дохода сотрудника = ", full_sal / sum_lines)

#Не сообразил как сделать конструкцию меньше.