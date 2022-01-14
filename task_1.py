import sys

try:
    hours, rate, reward = map(int, sys.argv[1:])  # принимаем аргументы из терминала и пытаемся привести к 'INT'
    # hours = int(sys.argv[1])
    # rate = int(sys.argv[2])
    # reward = int(sys.argv[3])

    salary = hours * rate + reward  # считаем ЗП по формуле
except ValueError as er:  # обрабатываем исключение
    print('Ошибка ввода аргументов!')
else:
    print(f'Наработано часов: {hours}\n'
          f'Ставка (тугриков в час): {rate}\n'
          f'Премия (бонусных тугриков): {reward}\n'
          f'ЗП (тугриков): {salary}\n'
          f'Не забудьте заплатить все налоги!')
