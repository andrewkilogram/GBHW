lesson = 'Урок 5, задание 2 \n'

print(lesson)
print('Выполнить подсчёт строк и слов в каждой строке.')

# lin_str = len(full_content[0].split())
# file_strings = "".join(map(str, full_content))

with open("count.txt", "r") as f:
    my_f = open("count.txt", "r")  # Не пойму как обойтись без этой строки, или нужно как-то изменить строку выше?
    full_content = my_f.readlines()
    len_full = len(full_content)
    for line in f:
        print(*line.split(), "-", len(line.split()), 'Elements in line')

print("\nTotal lines: ", len_full)
