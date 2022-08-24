print('Урок 7, задание 3')
print('Реализовать программу работы с органическими клетками. \n')
#Судя по условию задачи, результат должен отрисовывать указанные в make_order символы, но в данном примере из разбора дз этого нет.
class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, row):
        return '\n'.join(["🐙" * row for _ in range(self.nums // row)]) + "\n" + "😵" * (self.nums % row)

    def __str__(self):
        return f"{self.nums}"

    def __add__(self, other):
        print("Сложение")
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print("Вычитание")
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else "Меньше"

    def __mul__(self, other):
        print("Умножение")
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print("Деление")
        return Cell(self.nums // other.nums)

cell_1 = Cell(11)
cell_2 = Cell(12)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)