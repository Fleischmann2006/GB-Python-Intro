def is_number(a):
    """Проверяет, является ли аргумент числом

    :param a: аргумент для проверки
    :return: True - можно привести к float, False - нельзя
    """
    try:
        return float(a)
    except (TypeError, ValueError):
        print(f'{a} - не число')


def my_func(data, stop_symbol):
    """Выполняет поиск чисел и стоп-подстроки в строке.
       Пробел перед стоп-подстрокой нужно указывать при вызове функции (если требуется)

    :param data: строка данных для поиска чисел
    :param stop_symbol: стоп-символ, или подстрока, для завершения поиска
    :return: флаг указывающий, был ли обнаружен стоп-символ
    """
    stop_flag = False

    if data.find(stop_symbol) != -1:
        stop_flag = True                                # если нашли в строке стоп-символ(подстроку)
        data = data[:data.find(stop_symbol)].split()    # то обрезаем и разбиваем строку до этого символа
    else:
        data = data.split()                             # иначе разбиваем строку целиком

    for value in data:                                  # для каждой подстроки
        if is_number(value):                            # выполняем проверку на приведение к числовому типу
            global result
            result += float(value)                      # приводим и суммируем (глобальная переменная)

    return stop_flag                                    # сообщаем, если был обнаружен стоп-символ(подстрока)


result = 0

while True:
    user_input = input('Введите строку чисел, разделённых пробелами: ')

    if my_func(user_input, 'q'):                        # задал стоп-символ 'q' (без пробела!!!)
        print(f'Итоговая сумма введённых чисел: {result}')
        break                                           # выходим из цикла, если стоп-символ найден
    else:
        print(f'Промежуточная сумма введённых чисел: {result}')
