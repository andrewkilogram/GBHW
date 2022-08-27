print('Урок 8, задание 7')
print('Реализовать проект «Операции с комплексными числами». \n')

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.img = imaginary

    def __str__(self):
        return f'{self.real}+{self.img}j' if self.img > 0 else f'{self.real}{self.img}j'

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.img + other.img)

    def __mul__(self, other):
        return ComplexNumber((self.real * other.real - self.img * other.img),
                             (self.img * other.real + self.real * other.img))

cn = ComplexNumber(2, -2)
cn1 = ComplexNumber(2, -2)
check = (complex(2, -2) * complex(2, -2))
print(cn, "+", cn1, "=", cn + cn1)
print(cn, "*", cn1, "=", cn * cn1)
print("Проверка", check)