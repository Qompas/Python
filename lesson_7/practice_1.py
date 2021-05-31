# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])
        for row in matrix[1:]:
            if len(row) != self.columns:
                print("Матрица задана неправильно")
                self.matrix = []

    def __str__(self):
        string = ""
        maxlen = []
        for j in range(self.columns):
            maxlen.append(0)
        for i, row in enumerate(self.matrix):
            for j, el in enumerate(row):
                if maxlen[j] < len(str(el)):
                    maxlen[j] = len(str(el))
        for i, row in enumerate(self.matrix):
            for j, el in enumerate(row):
                string += str(el) + " " * (maxlen[j] - len(str(el)) + 3)
            string += "\n"
        return string

    def __add__(self, other):
        if (self.rows == other.rows) and (self.columns == other.columns):
            m = []
            for i in range(self.rows):
                m.append([])
                for j in range(self.columns):
                    m[i].append(self.matrix[i][j] + other.matrix[i][j])
            return Matrix(m)


matrix = Matrix([[12, 2, 3], [3, 213, 5]])
matrix = Matrix([[12, 2, 3], [3, 213333333333, 5], [4, 7, 3]]) + Matrix([[12, 1, 4], [3, 213, 3], [8, 9, 10]]) + Matrix(
    [[12, 1, 4], [3, 213, 3], [3, 7, 1]])
print(matrix)
