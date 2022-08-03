lesson = 'Урок 2, задание 2 \n'

print(lesson)
print('Реализовать структуру данных «Товары»')

goods_list = [] # Блок списка товаров
goods = goods_list

analytics = { # Блок аналитики
    "название": [],
    "цена": [],
    "количество": [],
    "ед": []
}

name_list = [] #Пустые списки для обавления в аналитику.
price_list = []
count_list = []
unit_list = []

goods_num = 1 #Нумерация товара

inp_start = 0

while inp_start == 0:  # Гл. меню
    print("Список текущих товаров: \n")
    for x in goods:
        print(x)
    print("\n1 - Просмотреть аналитику")
    print("2 - Добавление товара")
    print("3 - Выйти")

    inp_start = int(input("Введите пункт меню: "))

    if inp_start == 1:  # Меню аналитики

        if goods:
            print("Аналитика товаров\n")
            for x in analytics:
                print(x, analytics.get(x))
            inp_exit = (input("\nНажмите ENTER чтобы вернуться назад"))
            inp_exit = 0

        if not goods:
            print("Список товаров пуст\n")
            inp_exit = (input("Нажмите ENTER чтобы вернуться назад"))
            inp_exit = 0

        if inp_exit == 0:
            inp_start = 0

    if inp_start == 2:  # Меню товаров

        goods = []

        inp_add_goods = 0

        while inp_add_goods == 0:

            print("Список текущих товаров: \n")
            for x in goods:
                print(x)
            print(" \n1 - Добавить новый товар")
            print("2 - Выйти")

            inp_add_goods = int(input("Введите пункт меню: "))

            while inp_add_goods == 1:  # Цикл добавления

                cycle_add = {"название": "комп", "цена": "цена", "количество": "колич", "ед": "шт"} # Цикловой словарь, собирает параметры товара.

                # inp1 = 0 # Если лень вбивать параметры для проверки
                # inp2 = 0
                # inp3 = 0
                # inp4 = 0

                inp1 = (input("Введите название товара: "))
                inp2 = (input("Введите цену товара: "))
                inp3 = (input("Введите количество товара: "))
                inp4 = (input("Введите единицу измерения товара: "))

                cycle_add["название"] = inp1 #Значения ключей
                cycle_add["цена"] = inp2
                cycle_add["количество"] = inp3
                cycle_add["ед"] = inp4

                name_list.append(inp1) #Добавляем вводимые значения для блока аналитики в список
                price_list.append(inp2)
                count_list.append(inp3)
                unit_list.append(inp4)

                analytics["название"] = name_list #Добавляет список в блок аналитики
                analytics["цена"] = price_list
                analytics["количество"] = count_list
                analytics["ед"] = unit_list

                goods.append((goods_num, cycle_add)) #Закидывает цикловой словарь в список, добавляет номер.

                goods_num = goods_num + 1 #Наращивает номер

                print("Добавление товара: \n")
                for x in goods:
                    print(x)

                print(" \n1 - Добавить ещё")
                print("2 - Завершить")

                inp_add_goods = int(input("Введите пункт меню: "))

        if inp_add_goods == 2:
            inp_start = 0

    if inp_start == 3:
        print("ВСЕГО ХОРО ШЕГО")
        break
