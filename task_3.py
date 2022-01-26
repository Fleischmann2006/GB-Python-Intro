import sys


class Cell:
    def __init__(self, sub_cell=0):
        self.sub_cell = sub_cell    # целое неотрицательное число

    def __add__(self, other):
        return self.sub_cell + other.sub_cell

    def __sub__(self, other):
        return self.sub_cell - other.sub_cell if self.sub_cell >= other.sub_cell else print('Ошибка!')

    def __mul__(self, other):
        return self.sub_cell * other.sub_cell

    def __truediv__(self, other):
        return round(self.sub_cell / other.sub_cell) if other.sub_cell != 0 else print('Ошибка! Деление на ноль')

    @staticmethod
    def validate_input(input_data):
        try:
            int_input = int(input_data)
            if int_input <= 0:
                raise ValueError
        except (ValueError, TypeError):
            print('Ошибка ввода! Завершение работы')
            sys.exit()
        else:
            return int_input

    def make_order(self, order):
        print(''.join([f"{'*' * order}\n" for _ in range(self.sub_cell // order)]) + '*' * (self.sub_cell % order))


cell_1 = Cell()
cell_2 = Cell()

cell_1.sub_cell = Cell.validate_input(input('Введите число ячеек первой клетки: '))
cell_2.sub_cell = Cell.validate_input(input('Введите число ячеек второй клетки: '))

cell_1.make_order(Cell.validate_input(input('Введите порядок для первой клетки: ')))
cell_2.make_order(Cell.validate_input(input('Введите порядок для второй клетки: ')))

print(f'Сумма: {cell_1 + cell_2}')
print(f'Разность: {cell_1 - cell_2}')
print(f'Произведение: {cell_1 * cell_2}')
print(f'Частное: {cell_1 / cell_2}')
