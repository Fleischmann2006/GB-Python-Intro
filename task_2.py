class Road:
    # конструктор
    def __init__(self, length, width, density=25.0, thickness=5.0):
        """ Длина и ширина полотна являются обязательными атрибутами
        при создании экземпляра класса "Road"

        :param length: длина полотна (м)
        :param width: ширина полотна (м)
        :param density: плотность покрытия (кг/(м2*1см))
        :param thickness: толщина покрытия (см)
        """
        self._length = length
        self._width = width
        self._density = density
        self._thickness = thickness

    # методы класса
    def weight_calc(self):
        try:
            return round(float(self._width) * float(self._length)
                         * float(self._density) * float(self._thickness) / 1000, 3)
        except (TypeError, ValueError) as er:
            print(er)


my_road = Road(input('Введите длину дорожного покрытия: '), input('Введите ширину дорожного покрытия: '))
print(f'Масса покрытия: {my_road.weight_calc()} т.')
