from time import sleep


class TrafficLight:
    # атрибуты класса
    __color = ['Red', 'Yellow', 'Green']

    # конструктор
    def __init__(self):
        self.phase = 0
        self.cycle = 0

    # методы класса
    def running(self, cycles):
        if cycles == 0:
            print('Эмуляция бесконечной работы светофора')
        else:
            print(f'Эмуляция {cycles} циклов работы светофора')

        while cycles == 0 or self.cycle < cycles:
            if self.phase == 0:                 # красный 7 секунд
                self.phase = 1
                print(f'{self.__color[0]}')
                sleep(7)
            elif self.phase == 1:               # желтый 2 секунды
                self.phase = 2
                print(f'{self.__color[1]}')
                sleep(2)
            elif self.phase == 2:               # зеленый 5 секунд
                self.phase = 3
                print(f'{self.__color[2]}')
                sleep(5)
            else:                               # желтый 2 секунды
                self.phase = 0
                print(f'{self.__color[1]}')
                sleep(2)

                self.cycle += 1                 # инкремент счетчика циклов


# создаем экземпляр класса 'TrafficLight'
my_tl = TrafficLight()
try:
    # вызываем метод 'running' и передаём в него кол-во циклов работы светофора
    my_tl.running(int(input("Введите кол-во циклов работы светофора, или '0' для бесконечного цикла: ")))
except ValueError:
    print('Ошибка!')
finally:
    print('\nEND')
