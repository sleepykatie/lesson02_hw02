class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income   # {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        full_name = f'{self.surname} {self.name}'
        return full_name

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus'] * self._income['wage']
        return total_income

    def __str__(self):
        return str(self.__dict__)


Superworker = Position('John', 'Stone', 'Superworker', {'wage': 1000, 'bonus': 0.85})
print(Superworker)
print(Superworker.name)
print(Superworker.surname)
print(Superworker.position)
print(Superworker._income)

print('Full name: ', Superworker.get_full_name())
print('Total income: ', Superworker.get_total_income())

