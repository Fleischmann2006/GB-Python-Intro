class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} рисует квадрат')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} очерчивает круг')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} пачкает бумагу')


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

pen.draw()
pencil.draw()
handle.draw()
