def my_func(a, b, c):
    """Принимает три аргумента типа int/float
    и возвращает сумму двух наибольших

    :param a: первое число
    :param b: второе число
    :param c: третье число
    :return: сумма двух наибольших
    """
    try:
        numbers = [float(a), float(b), float(c)]    # Составляем последовательность
        numbers.remove(min(numbers))                # Убираем наименьший элемент по первому совпадению

    except (TypeError, ValueError) as er:
        print(f'Ошибка: {er}')
    else:
        return sum(numbers)                         # Возвращаем сумму оставшихся элементов


# Тест работы функции:
# print(my_func(13, 44.2, -28))
# print(my_func(13, 44.2, 13))
