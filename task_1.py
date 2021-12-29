# список с элементами различных типов
my_list = [321,                                                 # integer
           -9.999,                                              # float
           None,                                                # none
           'Nothing there!',                                    # string
           True,                                                # bool
           [1, 2, 3, 'GO!'],                                    # another list
           ('master', 'slave'),                                 # tuple
           {'first_name': 'Вася', 'second_name': 'Пупкин'},     # dict
           {'Санкт-Петербург', 'Москва', 'Мурманск'},           # set
           range(10)                                            # range
           ]

# нумеруем элементы списка, начиная с единицы, и выводим как их тип, так и сами элементы
for i, el in enumerate(my_list, 1):
    print(f'{i}) {type(el)} {el}')
