# test_str = '1 2 3 abc 45 18 qwe 67 765 as13df 87 -67.28 -42 67 as12.84 72.1'
result = []


class NotANumber(Exception):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return f'{self.val} - не число!'


def is_float(data):
    try:
        float(data)
    except ValueError:
        return False
    else:
        return True


while (user_input := input("Введите последовательность чисел, "
                           "разделённых пробелами, или 'q' для выхода: ")) != 'q':
    for word in user_input.split():
        try:
            if is_float(word):
                result.append(int(word) if float(word) % 1 == 0 else float(word))
            else:
                raise NotANumber(word)
        except NotANumber as er:
            print(er)

    print('Список чисел:', *result)
