lesson = 'Урок 4, задание 1 \n'

print(lesson)
print('Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.\n')

my_fact = 1 + int(input("Факториал числа: "))
newlist = range(1, my_fact)
def generator():
    f_num = 1
    for el in (newlist):
        yield f'!{el} = {f_num}'
        f_num *= el + 1
for el in generator():
    print(el)