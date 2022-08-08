lesson = 'Урок 3, задание 1 \n'

print(lesson)
print('Выполните возведение числа x в степень y.')

# def expon(arg_1, arg_2): #Решения запрещённое на территории Российской Федерации
# 1/    return arg_1 ** arg_2
# 2/    return pow(arg_1, arg_2)
# print(expon(2, -2))

def expon(arg_1, arg_2):
    if arg_1 <= 0 or arg_2 >= 0:
        print("Первое значение должно быть больше нуля, второе меньше.")
    else:
        res = 1
        for i in range(abs(arg_2)):
            res *= arg_1
        return 1 / res
print(expon(2, -4))
