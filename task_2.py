from abc import ABC, abstractmethod


class Clothes(ABC):
    # вводим ID товара и базу (словарь)
    item_id = 0
    base = {}

    # "универсальный" конструктор
    def __init__(self, param=0):
        self.param = param
        self.type = ''
        Clothes.item_id += 1
        self.item_id = Clothes.item_id  # присваиваем товару ID
        self.consumption = self.calc_cons  # считаем расход ткани сразу, при добавлении товара
        Clothes.base[Clothes.item_id] = self  # добавляем товар в базу

    # def __str__(self):
    #     print(f'   ID|   Type|  Param|   Cons')
    #     return '\n'.join([f'{key:>5} {value.type:>7} {value.param:>7} {value.consumption:>7}'
    #                       for key, value in Clothes.base.items()])

    @property
    @abstractmethod
    def calc_cons(self):
        pass

    # метод, позволяющий удалить товар из базы
    def rem(self):
        print(f'ID: {self.item_id} удалён из базы ({self.type} {self.param})')
        del Clothes.base[self.item_id]

    # метод, считающий общий расход ткани для товаров из базы
    @staticmethod
    def calc_total():
        return sum([value.consumption for value in Clothes.base.values()])

    # метод, отвечающий за вывод информации о товарах в базе
    @staticmethod
    def show_info():
        print('*' * 29)
        print(f'   ID|   Type|  Param|   Cons')
        [print(f'{key:>5} {value.type:>7} {value.param:>7} {value.consumption:>7}')
         for key, value in Clothes.base.items()]
        print('*' * 29)


# дочерний класс 'пальто'
class Coat(Clothes):
    def __init__(self, param):
        super().__init__(param)
        self.type = 'coat'
        print(f'ID: {self.item_id} добавлен в базу ({self.type}, {self.param})')

    @property
    def calc_cons(self):
        return round((self.param / 6.5 + 0.5), 2)


# дочерний класс 'костюм'
class Suit(Clothes):
    def __init__(self, param):
        super().__init__(param)
        self.type = 'suit'
        print(f'ID: {self.item_id} добавлен в базу ({self.type}, {self.param})')

    @property
    def calc_cons(self):
        return round((2 * self.param / 100 + 0.3), 2)  # не забываем перевести сантиметры (рост) в метры


# добавляем новые товары в базу
my_coat_1 = Coat(50)  # пальто 50 размера
my_suit_1 = Suit(180)  # костюм для роста 180см
my_suit_2 = Suit(192)  # костюм для роста 192см

# используем переопределённые методы для расчёта расхода ткани
print(f'Расход ткани на {my_coat_1.type} {my_coat_1.param} составляет: {my_coat_1.calc_cons}')
print(f'Расход ткани на {my_suit_1.type} {my_suit_1.param} составляет: {my_suit_1.calc_cons}')

# print(my_coat_1)
Clothes.show_info()     # выводим информацию из базы

my_suit_1.rem()         # удаляем товар из базы

my_coat_2 = Coat(55)    # добавляем ещё 1 товар в базу
# print(my_coat_2)
Clothes.show_info()     # выводим информацию из базы

# считаем общий расход ткани
print(f'Общий расход ткани: {Clothes.calc_total()}')
