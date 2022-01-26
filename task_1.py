a = [[1, -1, 26, 8], [-32, 5, 43, -3], [19, 2, -27, 4], [-4, -11, 4, 61]]
b = [[2, 4, 3, 2], [1, 7, 7, 1], [5, 5, 5, 5], [3, 9, 8, 6]]


def print_sep():
    print('*' * 20)


class Matrix:
    def __init__(self, m):
        self.m = m

    def __str__(self):
        # выводим построчно. Внутри строки разделяем через пробел и выравниваем по правому краю
        return '\n'.join([' '.join([f'{str(num):>3}' for num in string]) for string in self.m])

    def __add__(self, other):
        """
        Поэлементно суммируем элементы матриц

        Сложение идёт в порядке обхода элементов первой матрицы
        Обрабатываемые исключения:
            *) в первой матрице больше элементов, чем во второй
        Не обрабатываемое событие:
            *) в первой матрице меньше элементов, чем во второй,
            исключение не поднимается, лишние элементы не участвуют в расчёте
        """
        try:
            return Matrix([[(self.m[y][x] + other.m[y][x]) for x in range(len(self.m[y]))]
                           for y in range(len(self.m))])
        except IndexError as er:
            print('Ошибка! Разница в размерности матриц')


my_matrix_1 = Matrix(a)
my_matrix_2 = Matrix(b)

print_sep()
print(f'Первая матрица:\n{my_matrix_1}')
print_sep()
print(f'Вторая матрица:\n{my_matrix_2}')

print_sep()
print(f'Сумма матриц:\n{my_matrix_1 + my_matrix_2}')
