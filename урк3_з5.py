lesson = 'Урок 3, задание 5 \n'

print(lesson)
print('При нажатии Enter должна выводиться сумма введенных чисел.')

# numbs_list = [1, 2]
# add = []
# add = [int(x) for x in input("Введите элементы списка: ").split()]
# numbs_list.extend(add)
# sum_list = sum(numbs_list)
# print(numbs_list)
# print(add)
# print(sum_list)

#В этом задании придумал только конструкцию выше, ниже код который подсмотрел на разборе дз.
def sum_num():
    numbs_list = []
    sum = 0
    while True:
        err = False
        print("\nДля выхода из цикла введите wq")
        add = input("Введите элементы списка: \n").split()
        numbs_list.extend(add)
        for num in add:
            if num == "wq":
                return sum
            else:
                try:
                    sum += int(num)
                except:
                    err = True
                if err:
                    pass
        print("Сумма введеных числовых значений: \n", sum)
        print("Введеные значения: \n", numbs_list)
print(sum_num())
