import random
# работаем с файлом "text_5.txt"
# решил открывать файл на запись/чтение одновременно
with open('text_5.txt', 'w+', encoding='UTF-8') as fil:
    # и записываю в него 10 случайных числел от 1 до 100
    print(' '.join([str(random.randint(1, 100)) for i in range(10)]), file=fil)

    fil.seek(0)                 # возвращаем указатель в начало
    data = fil.read().strip()   # читаем строку чисел из файла и убираем '\n'
    print(f'Из файла "text_5.txt" прочитан следующий ряд чисел:\n{data}')
    # разбиваем строку с числами на список строк, затем приводим каждый элемент к целому числу и суммируем
    print(f'Сумма чисел равна: {sum(list(map(int, data.split())))}')

print('END')
