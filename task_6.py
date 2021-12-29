# реализуем "консольное" меню
# структура:
# add - добавить новый товар
# rem - удалить товар
# info - информация о товаре
# an - аналитика
# help - помощь
# q - выход
##########################################################################
good_dict_keys = ['название', 'цена', 'кол-во', 'ед. изм.']     # список ключей (характеристик) товара
goods = []                                                      # список товаров
goods_id = 0                                                    # ID товара
# goods_an = dict.fromkeys(good_dict_keys, [])

# основной цикл меню
while True:
    print('*' * 100)
    print('Главное меню')
    menu_cmd = input('Введите команду, или "help" для просмотра списка команд: ')

    if menu_cmd == 'q':             # завершение работы, выход из цикла по "стоп" слову
        print('END')
        break
    elif menu_cmd == 'help':        # отобразить список команд
        print('*' * 100)
        print('add - добавить новый товар')
        print('rem - удалить товар')
        print('info - информация о товаре')
        print('an - аналитика')
        print('back - возврат в главное меню')
        print('help - список команд')
        print('q - завершение работы и выход')
        print()
    elif menu_cmd == 'add':         # меню добавления нового товара
        print('*' * 100)
        print('Меню добавления новых товаров')
        print('Для возврата в главное меню введите "back"')
        print('Для просмотра списка товаров введите "info"')

        while True:                 # цикл для добавления нескольких товаров
            add_cmd = input('Введите название | стоимость | кол-во | ед. изм (через пробел): \n')

            if add_cmd == 'back':       # выйти в главное меню
                break
            elif add_cmd == 'info':     # показать список товаров
                if goods:
                    print('Список товаров:')
                    for good in goods:
                        print(good)
                    print()
                else:
                    print('Товары не зарегистрированы\n')
                continue
            else:
                add_cmd = add_cmd.split()   # пытаемся сформировать список характеристик нового товара

            new_goods = {}

            if len(add_cmd) != 4:           # проверяем, ввели ли необходимые 4 характеристики
                print('Вы ввели не все данные о товаре, или ввели лишние\n')
                continue
            else:
                for i in range(len(good_dict_keys)):
                    new_goods[good_dict_keys[i]] = add_cmd[i]

            # проверяем, что "цена" и "кол-во" указаны как числа
            if str(new_goods['цена']).strip().isdigit() and str(new_goods['кол-во']).strip().isdigit():
                goods_id += 1
                goods.append((goods_id, new_goods))     # добавляем товар в базу, если все данные указаны верно
                print('Новый товар добавлен: ')
                for item in new_goods.items():
                    print(': '.join(item))
                print()
            else:
                print('Вы неверно ввели данные товара\n')

    elif menu_cmd == 'rem':         # меню удаления товара
        if goods:
            print('*' * 100)
            print('Меню удаления товаров')
            print('Для возврата в главное меню введите "back"')
            print('Для просмотра списка товаров введите "info"')

            while True:
                rem_goods = {}

                # просим ввести ID товара, который нужно удалить
                rem_cmd = input('Введите ID товара, который хотите удалить: ')

                if rem_cmd == 'back':       # выйти в главное меню
                    break
                elif rem_cmd == 'info':     # показать список товаров
                    if goods:
                        print('Список товаров:')
                        for good in goods:
                            print(good)
                        print()
                    else:
                        print('Товары не зарегистрированы\n')
                elif rem_cmd.strip().isdigit():
                    rem_cmd = int(rem_cmd.strip())

                    j = 0
                    while j < len(goods):   # в цикле ищем товар по ID
                        if goods[j][0] == rem_cmd:  # и удаляем, если находим
                            rem_goods = goods[j][1]
                            goods.pop(j)
                            print('Товар успешно удалён из базы: ')
                            for item in rem_goods.items():
                                print(': '.join(item))
                            print()
                            break
                        j += 1
                    else:
                        print('ID товара не найден, воспользуйтесь командой "info"\n')
                else:
                    print('Некорректный ID\n')
        else:
            print('Товары не зарегистрированы\n')
    elif menu_cmd == 'info':    # показать список товаров
        if goods:
            print('*' * 100)
            print('Список товаров:')
            for good in goods:
                print(good)
            print()
        else:
            print('Товары не зарегистрированы\n')
    elif menu_cmd == 'an':  # показать аналитику
        if goods:
            goods_an = {'название': [], 'цена': [], 'кол-во': [], 'ед. изм.': []}

            for good in goods:                          # перебираем все товары по списку
                for key, value in good[1].items():      # получаем доступ к вложенным словарям по ключу и значению
                    if value not in goods_an[key]:      # решил убрать повторяющиеся значения по всем ключам
                        goods_an[key].append(value)     # заполняем списки в словаре аналитики

            print(goods_an)                             # печатаем аналитику

        else:
            print('Товары не зарегистрированы\n')
    else:
        print('Команда не распознана\n')
