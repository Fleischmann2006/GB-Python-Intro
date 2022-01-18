import re

# для каждой строки первое найденное слово используем в качестве ключа
# в строке ищем все числа, приводим их к 'int' и суммируем в значение
# собираем словарь
try:
    with open('text_6.txt', 'r', encoding='UTF-8') as fil:
        topic_dict = {re.search(r'\w+', topic).group(): sum(map(int, re.findall(r'\d+', topic)))
                      for topic in fil.readlines()}
        print(topic_dict)
except FileNotFoundError:
    print('Файл "text_6.txt" не найден!')

print('END')
