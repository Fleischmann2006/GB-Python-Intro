import json


def avg_pos_profit_calc(profit_dict):
    # фильтруем только положительные профиты
    profit_list = [profit for profit in profit_dict.values() if profit > 0]

    # возвращаем среднее
    return round(sum(profit_list) / len(profit_list), 2)


result = []
# для чтения используем файл "text_7.txt"
# проверяем, существует ли указанный файл
try:
    with open('text_7.txt', 'r', encoding='UTF-8') as fil1:
        try:
            company_profit_dict = {company[0]: int(company[2]) - int(company[3])
                                   for company in list(map(str.split, fil1.readlines()))}
            # print(company_profit_dict)
            avg_profit_dict = {'average_profit': avg_pos_profit_calc(company_profit_dict)}
            # print(avg_profit_dict)

            # формируем итоговый список из двух словарей
            result = [company_profit_dict, avg_profit_dict]
            print(result)
        except ValueError:
            print('Ошибка данных!')
except FileNotFoundError:
    print('Файл "text_7.txt" не найден!')

# для записи в формате 'json' используем файл "text_7.json"
if result:
    with open('text_7.json', 'w', encoding='UTF-8') as fil2:
        json.dump(result, fil2, ensure_ascii=False, indent=4)
        print(f'Запись в файл "{fil2.name}" успешно завершена')

print('END')
