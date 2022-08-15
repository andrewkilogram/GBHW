lesson = 'Урок 5, задание 7 \n'

print(lesson)
print( 'Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.')

import json

with open("text_77.json", "w", encoding="utf-8") as write_f, open("text_7.txt", encoding="utf-8") as text_file:
    profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in text_file}
    f_up = [i for i in profit.values() if i > 0]
    result = [profit, {"Средняя прибыль": round(sum(f_up) / len(f_up))}]
    json.dump(result, write_f, ensure_ascii=False, indent=4)

# Здесь я в итоге сдался и тоже взял решение с разбора дз.
# Изначально делал это задание на основе кода из задания 6, но не понял почему мой словарь в json'е формируется в строчку и для каждой компании отдельно.
# Больше всего конечно обидно что мой незаконченный код в 3 раза больше работающего примера.

# for line in text_file.readlines():
#     my_line = "".join((i if i in "0123456789" else " ") for i in line).split()
#     int_line = [int(i) for i in my_line]
#     result = int_line[0] - int_line[1]
#     result_plus = result > 0
#     if result_plus == True:
#         result_plus_clear = result
#         json_dict = {line.split()[0]: result_plus_clear}
#         json_str = str(json_dict)
#         write_f.write(json_str)
