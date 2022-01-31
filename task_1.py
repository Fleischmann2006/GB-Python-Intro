class Date:
    def __init__(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y

    def __str__(self):
        return f'Day: {self.day}\n' \
               f'Month: {self.month}\n' \
               f'Year: {self.year}'

    @staticmethod
    def val_date(data):
        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        d, m, y = data

        # проверяем год (любое число больше, либо равное 0)
        # до Н.Э. не учитываем
        y = y if y >= 0 else None

        # проверяем месяц
        m = m if 12 >= m >= 1 else None

        # проверяем день
        d = d if m is not None and days_per_month[m - 1] >= d >= 1 else None

        return d, m, y

    @classmethod
    def set_date(cls, data):
        data = data.split('-')

        try:
            data = list(map(int, data))

            if len(data) != 3:
                raise ValueError

            d, m, y = cls.val_date(data)

            if None in (d, m, y):
                raise DateIncorrect
        except (ValueError, DateIncorrect) as er:
            print('Error!')
            print(er)
        else:
            return cls(d, m, y)


class DateIncorrect(Exception):
    def __str__(self):
        return 'The date is incorrect'


while True:
    my_date = Date.set_date(input('Enter the date in format DD-MM-YYYY: '))
    if my_date:
        print(my_date)
        break

    print('Try again!')
