import sys
from abc import ABC, abstractmethod


# исключение, если товара с указанным ID нет на складе
class NotFound(Exception):
    def __init__(self, obj=0, obj_id=0):
        self.obj = obj
        self.obj_id = obj_id

    def __str__(self):
        if self.obj:
            return f'Ошибка! Товар в базе не найден!\n{self.obj}'
        else:
            return f'Ошибка! Товар в базе не найден! ID: {self.obj_id}'


# исключение, если товара не хватает
class NotEnough(Exception):
    def __init__(self, obj, qty1, qty2):
        self.obj, self.qty1, self.qty2 = obj, qty1, qty2

    def __str__(self):
        return f'Ошибка! Не хватает товара. Есть {self.qty1}, а нужно {self.qty2}\n{self.obj}'


# несуществующая категория товаров
class UnresolvedEq(Exception):
    def __init__(self, name, names):
        self.name, self.names = name, names

    def __str__(self):
        return f'Указанная категория "{self.name}" не разрешена\nИспользуйте: {" ".join(self.names)}'


# ошибка ввода параметров товара
class InputError(Exception):
    def __str__(self):
        return 'Ошибка ввода параметров товара\nПопробуйте ещё раз'


# класс описывает склад/организацию/место хранения
class Warehouse:
    def __init__(self, name):
        self.name = name
        self.__goods = {}
        self.__goods_id = 0

    # выводит перечень всех товаров, имеющихся на складе
    def __str__(self):
        if self.__goods:
            return ('*' * 100) + f'\n"{self.name}". Полный перечень товаров:\n' + \
                   '\n'.join([f'ID: {k}. {g[0]} | Кол-во: {g[1]}'
                              for k, g in self.__goods.items()])
        else:
            return ('*' * 100) + f'\nНа складе "{self.name}" пусто'

    # метод добавляет товар на склад
    def add(self, new_good, qty):
        print('*' * 100)
        if found_id := self.__search(new_good):       # если товар уже в базе, меняем кол-во
            self.__set_qty(found_id, self.__get_qty(found_id) + qty)
            print(f'{self.name}. Кол-во изменилось. ID: {found_id}')
        else:                                         # иначе добавляем новую позицию
            self.__goods_id += 1
            self.__goods[self.__goods_id] = [new_good, qty]
            found_id = self.__goods_id
            print(f'{self.name}. Добавлен новый товар. ID: {found_id}')
        print(f'{self.__get_pos(found_id)} | Кол-во: {self.__get_qty(found_id)} (+{qty})')

    # метод удаляет/списывает товар со склада
    def rem(self, rem_good, qty):
        print('*' * 100)
        try:
            # выполняем поиск ID, или самого товара
            if found_id := self.__search(rem_good):
                if self.__get_qty(found_id) > qty:
                    self.__set_qty(found_id, self.__get_qty(found_id) - qty)
                    print(f'{self.name}. Кол-во изменилось. ID: {found_id}')
                    print(f'{self.__get_pos(found_id)} | Кол-во: {self.__get_qty(found_id)} (-{qty})')
                    return self.__get_pos(found_id), qty
                elif self.__get_qty(found_id) == qty:
                    print(f'{self.name}. Товар закончился. ID: {self.__goods_id}')
                    print(f'{self.__get_pos(found_id)}')
                    return tuple(self.__goods.pop(found_id))
                else:
                    raise NotEnough(rem_good, self.__get_qty(found_id), qty)
            else:
                raise NotFound(obj=rem_good)
        except (NotFound, NotEnough) as er:
            print(er)

    @staticmethod
    def move(wh1, wh2, m_id, qty):
        print('*' * 100)
        print(f'Перемещение {qty} ед. товара ID: {m_id}\nИсточник: {wh1.name}\nЦель: {wh2.name}')
        try:
            if m_id in wh1.__goods.keys():
                if obj := wh1.rem(wh1.__get_pos(m_id), qty):
                    wh2.add(*obj)
            else:
                raise NotFound(obj_id=m_id)
        except NotFound as er:
            print(er)

    # метод возвращает товар с указанным ID
    def __get_pos(self, pos_id):
        return self.__goods[pos_id][0]

    # метод возвращает кол-во товара с указанным ID
    def __get_qty(self, pos_id):
        return self.__goods[pos_id][1]

    # метод изменяет кол-во товара
    def __set_qty(self, pos_id, new_qty):
        self.__goods[pos_id][1] = new_qty

    # метод выполняет поиск товара на складе и возвращает ID, если находит
    def __search(self, pos):
        for k in self.__goods.keys():
            if set(self.__get_pos(k).get_params) == set(pos.get_params):
                return k


# основной класс (описывает общие характеристики товара)
class Equipment(ABC):
    def __init__(self, vendor, price):
        self.params = []
        self.vendor = vendor
        self.price = price
        self.params += self.vendor, self.price

    def __str__(self):
        return f'Пр-во: {self.vendor} | Цена: {self.price}р'

    @property
    def get_params(self):
        return self.params

    @staticmethod
    def def_type(data, types):
        try:
            data = data.split()
            if data[0] in types:
                if data[0] == types[0]:     # принтер
                    result = Printer.val_data(data[1:])
                elif data[0] == types[1]:   # сканер
                    result = Scanner.val_data(data[1:])
                else:                       # измельчитель
                    result = Shredder.val_data(data[1:])
            else:
                raise UnresolvedEq(data[0], types)
        except (TypeError, ValueError, UnresolvedEq) as er:
            print(er)
        else:
            try:
                if result:
                    return result
                else:
                    raise InputError
            except InputError as er:
                print(er)

    @staticmethod
    def is_price(price):
        try:
            return float(price)
        except ValueError:
            return False

    @staticmethod
    def val_number(is_id=False):
        while (number := input(f'Введите {"ID" if is_id else "кол-во"}: ')) != 'q':
            try:
                return abs(int(number))     # а вот так!
            except ValueError:
                print('Ошибка! Вы ввели не число!')
        else:
            sys.exit()

    @classmethod
    @abstractmethod
    def val_data(cls, data):
        pass


# дочерний класс 'Принтер' с уникальными для него аргументами
class Printer(Equipment):
    def __init__(self, vendor, price, c_type='-', p_format='-'):
        super().__init__(vendor, price)
        self.e_type = 'Принтер'
        self.c_type = c_type
        self.p_format = p_format
        self.params += self.e_type, self.c_type, self.p_format

    def __str__(self):
        return f'{self.e_type} {self.c_type} формата {self.p_format}\n' + super().__str__()

    @classmethod
    def val_data(cls, data):
        if 2 <= len(data) <= 4:
            if price := Equipment.is_price(data[1]):
                data[1] = price
                return cls(*data)


# дочерний класс 'Сканер' с уникальными для него аргументами
class Scanner(Equipment):
    def __init__(self, vendor, price, color='ч/б', p_format='-'):
        super().__init__(vendor, price)
        self.e_type = 'Сканер'
        self.color = color
        self.p_format = p_format
        self.params += self.e_type, self.color, self.p_format

    def __str__(self):
        return f'{self.e_type} {self.color} формата {self.p_format}\n' + super().__str__()

    @classmethod
    def val_data(cls, data):
        if 2 <= len(data) <= 4:
            if price := Equipment.is_price(data[1]):
                data[1] = price
                return cls(*data)


# дочерний класс 'Измельчитель' с уникальными для него аргументами
class Shredder(Equipment):
    def __init__(self, vendor, price, power='-'):
        super().__init__(vendor, price)
        self.e_type = 'Измельчитель'
        self.power = power
        self.params += self.e_type, self.power

    def __str__(self):
        return f'{self.e_type} бумаги мощностью {self.power}Вт\n' + super().__str__()

    @classmethod
    def val_data(cls, data):
        if 2 <= len(data) <= 3:
            if price := Equipment.is_price(data[1]):
                data[1] = price
                return cls(*data)


def show_help(types):
    print('*' * 100)
    print('Введите категорию и характеристики товара в формате:\n'
          'категория хар1 хар2 .. харN\n'
          f'Доступные категории: {" ".join(types)}\n'
          'Доступные характеристики:\n'
          'Принтер - производитель, цена, тип печати, формат бумаги\n'
          'Сканер - производитель, цена, цветной или ч/б, формат бумаги\n'
          'Измельчитель - производитель, цена, мощность(Вт)')
    print()


wh_names = ['Главный склад', 'МосГорЭкспертиза', 'Рога и Копыта']
eq_types = ['Принтер', 'Сканер', 'Измельчитель']
wh_dict = {name: Warehouse(name) for name in wh_names}

# добавляем несколько товаров вручную
wh_dict['Главный склад'].add(Printer(vendor='HP', price=12500.0, c_type='струйный', p_format='A3'), 3)
wh_dict['Главный склад'].add(Scanner(vendor='Canon', price=3500.0, color='цветной', p_format='A4'), 2)
wh_dict['Главный склад'].add(Shredder(vendor='Brauberg', price=8200.0, power='1200'), 4)
wh_dict['МосГорЭкспертиза'].add(Scanner(vendor='Canon', price=3500.0, color='цветной', p_format='A4'), 9)
wh_dict['Рога и Копыта'].add(Printer(vendor='HP', price=12500.0, c_type='струйный', p_format='A3'), 2)


# основной цикл меню
while True:
    print('*' * 100)
    print('Главное меню')
    print('Доступные склады:')
    print('\n'.join([f'{num}) {name}' for num, name in enumerate(wh_names, 1)]))
    menu_cmd = input('Введите название склада, или "q" для выхода: ')

    if menu_cmd == 'q':             # завершение работы, выход из цикла по "стоп" слову
        print('END')
        break
    elif menu_cmd in wh_names:
        wh_name = menu_cmd
        while True:
            print('*' * 100)
            print(f'Меню склада "{wh_name}"')
            wh_cmd = input('Введите команду, или "help" для просмотра списка команд: ')

            if wh_cmd == 'q':
                print('END')
                sys.exit()
            elif wh_cmd == 'back':              # выйти в главное меню
                break
            elif wh_cmd == 'help':              # отобразить список команд
                print('*' * 100)
                print('add - добавить новый')
                print('rem - удалить/списать')
                print('move - перемещение')
                print('info - сводка по складу')
                print('back - возврат в главное меню')
                print('help - список команд')
                print('q - завершение работы и выход')
                print()
            elif wh_cmd == 'info':              # показать список товаров на выбранном складе
                print(wh_dict[wh_name])
            elif wh_cmd == 'add':               # меню добавления товаров
                print('*' * 100)
                print(f'Меню добавления новых товаров на склад "{wh_name}"')
                print('Для возврата в меню склада введите "back"')
                print('Для просмотра списка товаров введите "info"')
                print('Для просмотра инструкции введите "help"')

                while True:                     # цикл для добавления нескольких товаров
                    add_cmd = input('Введите категорию и характеристики товара:\n')

                    if add_cmd == 'q':
                        print('END')
                        sys.exit()
                    elif add_cmd == 'back':     # выйти в меню склада
                        break
                    elif add_cmd == 'info':     # показать список товаров
                        print(wh_dict[wh_name])
                    elif add_cmd == 'help':
                        show_help(eq_types)
                    elif add_obj := Equipment.def_type(add_cmd, eq_types):  # определяем дочерний класс
                        if add_qty := Equipment.val_number():               # получаем и проверяем кол-во
                            wh_dict[wh_name].add(add_obj, add_qty)          # добавляем в базу
                            print('*' * 100)

            elif wh_cmd == 'rem':               # меню удаления товаров
                print('*' * 100)
                print(f'Меню списания товаров со склада "{wh_name}"')
                print('Для возврата в меню склада введите "back"')
                print('Для просмотра списка товаров введите "info"')
                print('Для просмотра инструкции введите "help"')

                while True:                     # цикл для списания нескольких товаров
                    rem_cmd = input('Введите категорию и характеристики товара:\n')

                    if rem_cmd == 'q':
                        print('END')
                        sys.exit()
                    elif rem_cmd == 'back':     # выйти в меню склада
                        break
                    elif rem_cmd == 'info':     # показать список товаров
                        print(wh_dict[wh_name])
                    elif rem_cmd == 'help':
                        show_help(eq_types)
                    elif rem_obj := Equipment.def_type(rem_cmd, eq_types):  # определяем дочерний класс
                        if rem_qty := Equipment.val_number():               # получаем и проверяем кол-во
                            wh_dict[wh_name].rem(rem_obj, rem_qty)          # удаляем кол-во товаров из базы
                            print('*' * 100)

            elif wh_cmd == 'move':              # меню перемещения товаров
                print('*' * 100)
                print(f'Меню перемещения товаров со склада')
                print('Для возврата в меню склада введите "back"')
                print('Для просмотра списка товаров введите "info"')

                while True:                     # цикл для перемещения нескольких товаров
                    print('Доступные склады:')
                    print('\n'.join([f'{num}) {name}' for num, name in enumerate(wh_names, 1)]))
                    move_cmd = input('Введите название целевого склада:\n')

                    if move_cmd == 'q':
                        print('END')
                        sys.exit()
                    elif move_cmd == 'back':     # выйти в меню склада
                        break
                    elif move_cmd == 'info':     # показать список товаров
                        print(wh_dict[wh_name])
                    elif move_cmd in wh_names:
                        if move_cmd == wh_name:
                            print('Нельзя перемещять товар на тот же склад!\n'
                                  'Попробуйте указать другой склад\n')
                        else:
                            if (move_id := Equipment.val_number(is_id=True)) and (move_qty := Equipment.val_number()):
                                Warehouse.move(wh_dict[wh_name], wh_dict[move_cmd], move_id, move_qty)
                                print('*' * 100)
                    else:
                        print('Команда не распознана\n')
            else:
                print('Команда не распознана\n')
    else:
        print('Команда не распознана\n')
