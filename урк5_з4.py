lesson = 'Урок 5, задание 4 \n'

print(lesson)
print('Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские.')

from googletrans import Translator

myfile_en = open("text_4.txt", "r", encoding="utf-8")
read_file = myfile_en.read()
result = Translator().translate(read_file, dest='ru').text
myfile_ru = open("text_4_trns.txt", "w", encoding="utf-8")
myfile_ru.write(result)
