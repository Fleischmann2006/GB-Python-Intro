# Запрашиваем число у пользователя
number = int(input('Введите целое число (больше, либо равное нулю): '))
max_digit = 0

# Перебираем цифры в цикле
while number != 0:
    last_digit = number % 10
    number //= 10

    if last_digit > max_digit:
        max_digit = last_digit

# Благополучно вышли из цикла и выводим результат
print('Самая большая цифра: {}'.format(max_digit))
