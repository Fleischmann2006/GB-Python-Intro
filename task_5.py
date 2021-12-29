# существующий "изначальный" рейтинг
my_list = [7, 5, 3, 3, 2]

print(f'Изначальный рейтинг: \n{my_list}')
# запускаем цикл обработки пользовательского ввода
while True:
    user_input = input('Введите целое неотрицательное число, или "q" для завершения: ')  # запрос нового числа

    if user_input == 'q':               # выходим по "стоп" слову
        break
    elif user_input.strip().isdigit():  # проверка ввода
        new_number = int(user_input)    # приведём тип заранее, для лучшей читаемости далее

        if new_number > my_list[0]:     # если число самое большое, то автоматом ставим его в начало списка
            my_list.insert(0, new_number)
        else:                           # иначе в цикле ищем его место в рейтинге (в обратном порядке!)
            for i, el in enumerate(reversed(my_list)):
                if new_number <= el:
                    # можно вставить, используя срезы, можно, используя ".insert()"
                    # my_list = my_list[:len(my_list) - i] + [new_number] + my_list[len(my_list) - i:]
                    my_list.insert(len(my_list) - i, new_number)
                    break

        print(my_list)
    else:
        print('Ошибка ввода')
