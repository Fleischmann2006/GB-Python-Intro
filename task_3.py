class Worker:
    # конструктор
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    def get_income(self):
        return self._income


class Position(Worker):
    # методы класса
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


worker_1 = Position('Вася', 'Пупкин', 'Главный инженер', 120000.0, 60000.0)
print(worker_1.get_full_name())
print(worker_1.get_total_income())
print(worker_1.name)
print(worker_1.surname)
print(worker_1.position)
print(worker_1.get_income())  # используя "геттер"
