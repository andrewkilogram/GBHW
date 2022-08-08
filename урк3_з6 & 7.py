lesson = 'Урок 3, задание 6 & 7 \n'

print(lesson)
print('Реализовать функцию принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой.')
print('Продолжить работу над заданием, нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.\n')

def int_func(*args):
    args = input('Слова из маленьких латинских букв: ').split()
    args_list = str(args)
    args_up = args_list.title()

    alphabet = set('qwertyuiopasdfghjklzxcvbnm')
    if alphabet.isdisjoint(args_list.lower()) == True:
        print("Используйте латинский алфавит")
    else:
        return args_up
print(int_func())
