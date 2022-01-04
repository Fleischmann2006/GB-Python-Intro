# тестовая строка
# nice авп ъghj jапро hjjпаро вапрghgh cool Man auto autO zaz

def is_small_latin_word(word):
    """Проверяет, составлено ли слово только из маленьких букв латинского алфавита

    :param      word: слово для проверки
    :return:    True - если word состоит  только из маленьких букв латинского алфавита
                False - если обнаружены заглавные буквы, кириллица, различные символы
    """
    for letter in word:
        if ord(letter) < 97 or ord(letter) > 122:    # 97 - unicode 'a', 122 - unicode 'z'
            return False

    return True


def int_func(word):
    """Принимает слово, и если оно состоит только из маленьких букв латинского алфавита,
        меняет первую букву на заглавную

    :param word:    слово для проверки
    :return:        Word, если слово прошло проверку
                    None, если слово не прошло проверку, или аргумент не строка
    """
    if isinstance(word, str) and is_small_latin_word(word):
        return word.title()

    return None


# основная программа с пользовательским вводом
# тестовая строка
# nice авп ъghj jапро hjjпаро вапрghgh cool Man auto autO zaz
# ****************************************************************************
# Просим пользователя ввести строку, а затем разбиваем её на список слов
user_input = input('Введите строку из слов, разделённых пробелом: ').split()

# применяем int_func() к каждому слову из списка
# и отфильтровываем None, объединяя оставшиеся слова в результирующую строку
print(' '.join(list(filter(None, map(int_func, user_input)))))
