my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять',
           'Six': 'Шесть', 'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Девять', 'Zero': 'Ноль'}

# для чтения используем файл "text_4.txt"
# для записи используем файл "text_4_tr.txt"
# проверяем, существует ли первый файл
try:
    with open('text_4.txt', 'r', encoding='UTF-8') as fil1, open('text_4_tr', 'w', encoding='UTF-8') as fil2:
        translated_strings = [' '.join([my_dict.get(word, word) for word in string.split()]) + '\n'
                              for string in fil1.readlines()]
        fil2.writelines(translated_strings)
except FileNotFoundError:
    print('Файл "text_4.txt" не найден!')

print('END')
