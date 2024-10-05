# TODO здесь писать код
class Matrix:
    def __init__(self, row, column):
        self.row = row
        self. column = column
        self.data = None

    def add(self, matrix_2):
        if self.row == matrix_2.row and self.column == matrix_2.column:
            new_matrix = [[self.data[row][elem] + matrix_2.data[row][elem] for elem in range(self.column)]
                          for row in range(self.row)]
            return new_matrix
        else:
            print('Нельзя сложить данные матрицы. (Количество строк и столбцов у матрицы должны быть равны)')

    def subtract(self, matrix_2):
        if self.row == matrix_2.row and self.column == matrix_2.column:
            new_matrix = [[self.data[row][elem] - matrix_2.data[row][elem] for elem in range(self.column)]
                      for row in range(self.row)]
            return new_matrix
        else:
            print('Нельзя вычесть данные матрицы. (Количество строк и столбцов у матрицы должны быть равны)')

    def multiply(self, matrix_2):
        if self.column == matrix_2.row:
            res_matrix = []
            for i in range(self.row):
                new_matrix = []
                for j in range(matrix_2.column):
                    elem = 0
                    for k in range(self.column):
                        elem += self.data[i][k] * matrix_2.data[k][j]
                    new_matrix.append(elem)
                res_matrix.append(new_matrix)
            return res_matrix
        else:
            print('Две матрицы можно умножить друг на друга только в том случае, если количество столбцов первой матрицы равно количеству строк второй матрицы.')

    def transpose(self):
        result = []
        for i in range(self.column):
            new_matrix = []
            for j in range(self.row):
                new_matrix.append(self.data[j][i])
            result.append(new_matrix)
        return result

def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end = '\t')
        print('\n')

# Примеры работы с классом:

# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

# Тестирование операций
print("Матрица 1:")
print_matrix(m1.data)

print("Матрица 2:")
print_matrix(m2.data)

print("Сложение матриц:")
print_matrix(m1.add(m2))

print("Вычитание матриц:")
print_matrix(m1.subtract(m2))

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("Умножение матриц:")
print_matrix(m1.multiply(m3))

print("Транспонирование матрицы 1:")
print_matrix(m1.transpose())