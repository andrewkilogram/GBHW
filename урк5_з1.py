lesson = 'Урок 5, задание 1 \n'

print(lesson)
print('Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. ')

while True:
    myfile = open(r"z1.txt", "a", encoding="utf-8")
    file_inp = [input("Введите строку: ")]
    with myfile as file:
        for line in file_inp:
            file.write(line + '\n')
            x = len(line)
    if x == 0:
        myfile.close()
        print("Строка пуста")
        break
