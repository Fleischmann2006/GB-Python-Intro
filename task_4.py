numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# с использованием медода 'count' для поиска кол-ва вхождений
print([number for number in numbers if numbers.count(number) == 1])
