def salary_parse(file):
    """ Принимает файл с перечнем сотрудников и их окладов
        на каждой итерации возвращает оклад очередного сотрудника
        и обрабатывает ошибки в строках исходного файла

    :param file: файл для валидации
    :yield: величина оклада
    """
    i = 0
    salary_avg = 0

    for employee in file.readlines():
        try:
            salary = float(employee.strip().split()[1])

            if salary < 20000.0:
                print(''.join(employee[:-1]))

            salary_avg += salary
            i += 1
        except (TypeError, ValueError):
            print(f'Ошибка данных! {i + 1} строка')

    return salary_avg / i


# для работы используем файл "text_3.txt"
# проверяем, существует ли указанный файл
try:
    with open('text_3.txt', 'r', encoding='UTF-8') as fil:
        print('*' * 50)
        print('Сотрудники с окладом менее 20000:')
        print(f'\nСредняя величина оклада: {round(salary_parse(fil), 2)}')
except FileNotFoundError:
    print('Файл "text_3.txt" не найден!')

print('END')
