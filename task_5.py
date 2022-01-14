from functools import reduce

# список чётных чисел от 100 до 1000, включая границы
print([number for number in range(100, 1001, 2)])

# используем reduce() и лямбда-функцию для последовательного перемножения всех числел последовательности
print(reduce(lambda a, b: a * b, [number for number in range(100, 1001, 2)]))
