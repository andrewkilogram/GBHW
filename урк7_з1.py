print('Урок 7, задание 1')
print('Реализовать класс Matrix (матрица). \n')

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(' '.join([f'{i:0}' for i in line]) for line in self.matrix)

    def __add__(self, other):
        m = [[int(self.matrix[line][i]) + int(other.matrix[line][i]) for i in range(len(self.matrix[line]))] for line in range(len(self.matrix))]
        return Matrix(m)
        pass

matrix_1 = Matrix([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
matrix_2 = Matrix([[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]])

print(matrix_1)
print()
print(matrix_2)
mm = matrix_1 + matrix_2
print()
print(mm)