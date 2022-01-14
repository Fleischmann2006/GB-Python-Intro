from itertools import count, cycle

# первая часть скрипта
print('*' * 50)
print('Первый скрипт выводит список из 10 целых чисел, начиная с указанного')
num = int(input('Введите целое положительное число: '))
result = []

for i in count(num):
    if i >= num + 10:
        break
    else:
        result.append(i)

print(f'Результат: {result}\n')

# вторая часть скрипта
print('*' * 50)
print('Второй скрипт формирует список строк из введенных через пробел элементов, и повторяет их ещё 2 раза')
my_list = input('Введите элементы списка, разделенные пробелами: ').split()

result.clear()

for j, el in enumerate(cycle(my_list)):
    if j >= len(my_list) * 3:
        break
    else:
        result.append(el)

print(f'Результат: {result}\n')
