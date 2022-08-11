lesson = 'Урок 4, задание 1 \n'

print(lesson)
print('Реализовать два небольших скрипта:\n'
      '-итератор, генерирующий целые числа, начиная с указанного;\n'
      '-итератор, повторяющий элементы некоторого списка, определённого заранее.\n')

from itertools import count, cycle
import random

# ns = 100
# nf = ns + 100
# nc = 10
# list_sam = random.sample(range(ns, nf), nc)
# list_ran = random.randint(ns,nf)
# print(*list_sam)

#Я видно не понял задания, изначально пытался сделать генератор рандомных целых чисел и дальше уже отталкиваться от него, но в итоге решил дождаться разбора дз, оказывается всё было проще.

my_count = count(1)
my_cycle = cycle("ABCDF")
for _ in range(5):
      print(next(my_count), "-", next(my_cycle))

