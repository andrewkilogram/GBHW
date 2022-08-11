lesson = 'Урок 4, задание 4 \n'

print(lesson)
print('Определите элементы списка, не имеющие повторений.')

mylist = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
next_list = {i: 0 for i in mylist}
for i in mylist:
    next_list[i] +=1
print(*[i for i in next_list if next_list[i] == 1])

# [23, 1, 3, 10, 4, 11]