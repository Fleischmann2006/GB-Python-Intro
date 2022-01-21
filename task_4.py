from random import randint


# выводит информацию: является ли машина полицейской
def car_info(car):
    print(f'{car.color} {car.name}: {"полиция" if car.is_police else "гражданский"}')


class Car:
    direction_list = ['прямо', 'назад', 'налево', 'направо']

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} начал(а) движение')

    def stop(self):
        print(f'{self.color} {self.name} остановился(ась)')

    def turn(self):
        direction = self.direction_list[randint(0, 3)]

        if direction == 'прямо' or direction == 'назад':
            print(f'{self.color} {self.name} едет {direction}')
        else:
            print(f'{self.color} {self.name} повернул(а) {direction}')

    def show_speed(self):
        print(f'{self.color} {self.name} едет со скоростью {self.speed} км/ч')


class TownCar(Car):
    speed_limit = 60

    def show_speed(self):
        if self.speed > self.speed_limit:
            print(f'{self.color} {self.name} {self.speed} км/ч! Превышение скорости!')
        else:
            super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    speed_limit = 40

    def show_speed(self):
        if self.speed > self.speed_limit:
            print(f'{self.color} {self.name} {self.speed} км/ч! Превышение скорости!')
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


town_car = TownCar(5, 'черный', 'KIA')
work_car = WorkCar(20, 'красный', 'Nissan')
sport_car = SportCar(120, 'желтый', 'Lexus')
police_car = PoliceCar(60, 'белый', 'Ford')

print('*' * 50)
car_info(town_car)
car_info(work_car)
car_info(sport_car)
car_info(police_car)
print('*' * 50)

town_car.go()
town_car.show_speed()
town_car.turn()
town_car.speed = 65
town_car.show_speed()
town_car.speed = 30
town_car.turn()
town_car.stop()
print('*' * 50)

work_car.go()
work_car.show_speed()
work_car.turn()
work_car.speed = 42
work_car.show_speed()
work_car.speed = 10
work_car.turn()
work_car.stop()
print('*' * 50)

sport_car.show_speed()
sport_car.turn()
sport_car.speed = 0
sport_car.show_speed()
sport_car.stop()
sport_car.color = 'хлам'
print(f'{sport_car.name} попал в ДТП и превратился в {sport_car.color}')
print('*' * 50)

police_car.show_speed()
police_car.speed = 40
police_car.show_speed()
police_car.stop()
police_car.go()
police_car.turn()
