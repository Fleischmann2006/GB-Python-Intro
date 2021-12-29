# запрос ввода элементов списка
# элементы хранятся в списке в строковом виде, распознавание типа данных не производится
my_list = list()

while True:
    el = input('Введите следующий элемент списка, или "", чтобы завершить: ')

    if el:                      # добавляем новый элемент в список, если пользователь его ввёл
        my_list.append(el)
    else:                       # иначе выходим из цикла
        break

print(my_list)  # выводим изначальный вариант списка

# работаем с индексами с шагом 2 (не забывая про IndexError от последнего элемента)
for i in range(0, len(my_list) - 1, 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]     # "переворачиваем" два соседних элемента

print(my_list)  # выводим вариант списка с переставленными элементами
