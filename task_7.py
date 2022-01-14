def fact(num):
    factorial = 1

    for i in range(1, num + 1):
        if i == 1:
            yield 1
        else:
            factorial *= i
            yield factorial


print('Формирует список из факториалов чисел от 1 до указанного (включительно)')
print([el for el in fact(int(input('Введите целое положительное число: ')))])
