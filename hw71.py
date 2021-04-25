''' Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.'''

class Matrix:
    def __init__(self, element_of_matrix):
        self.element_of_matrix = element_of_matrix

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.element_of_matrix])

    def __add__(self, other):
        answer = 'Answer:\n'
        if len(self.element_of_matrix) == len(other.element_of_matrix):
            for line_1, line_2 in zip(self.element_of_matrix, other.element_of_matrix):
                if len(line_1) != len(line_2):
                    return 'Error, you have problem with matrix.'

                summed_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join(map(str, summed_line)) + '\n'
        else:
            return 'Error, you have problem with matrix.'
        return answer

matrix_1 = Matrix([[5, 4], [1, 5], [1, 4], [42, 33]])
matrix_2 = Matrix([[-1, 3], [5, 7], [61, 8], [-10, -20]])
matrix_3 = Matrix([[5, 4, 2], [1, 5, 4], [1, 4, 1], [42, 33, 5]])
print(matrix_1 + matrix_2)
print(matrix_1 + matrix_3)