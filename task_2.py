# для работы используем файл "text_1.txt" из первой задачи
# проверяем, существует ли указанный файл
try:
    with open('text_1.txt', 'r', encoding='UTF-8') as fil:
        str_num = 0

        for string in fil.readlines():
            str_num += 1

            # считаем слова, определяя их как конструкции, разделённые пробелом
            # решил вычистить спец.символы
            print(f'{str_num}-ая строка: {len(string.strip().split())} слов(а)')

        print(f'Всего: {str_num} строк')
except FileNotFoundError:
    print('Файл "text_1.txt" не найден!')

print('END')
