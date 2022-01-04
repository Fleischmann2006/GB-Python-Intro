def dev_float_func(a, b):
    """Возвращает результат деления двух чисел в типе/формате 'float'.
    Если аргументы переданы строками, выполняет поиск и замену
    запятой на точку и только после этого пытается привести аргументы
    к типу 'float'.

    Обрабатываются ошибки:
    1) неверный тип данных для переданного аргумента
    2) невозможность приведения к типу 'float'
    3) деление на ноль

    Позиционные аргументы:
    a - делимое
    b - делитель

    """
    if isinstance(a, str):
        a = a.replace(',', '.')
    if isinstance(b, str):
        b = b.replace(',', '.')

    try:
        a = float(a)
        b = float(b)
    except (TypeError, ValueError) as er:
        print(f'Ошибка: {er}')
    else:
        try:
            return a / b
        except ZeroDivisionError as er:
            print(f'Ошибка: {er}')


while True:
    print('*' * 50)
    print("Для выхода введите 'q'")
    print('Функция выполняет деление первого введённого числа на второе и выводит результат')

    num_1 = input('Введите первое число: ')
    if num_1 == 'q':
        break

    num_2 = input('Введите второе число: ')
    if num_2 == 'q':
        break

    print(f'Результат: {dev_float_func(num_1, num_2)}')
