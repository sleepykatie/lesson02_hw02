from random import randint


class Car:

    def __init__(self, speed, colour, name, is_police=False):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            return f'{self.colour} {self.name} went'

    def stop(self):
        if self.speed == 0:
            return f'{self.colour} {self.name} stopped'

    def turn(self, direction):
        if self.speed > 0:
            direction_comp = direction
            if direction_comp.casefold() == 'left':
                return f'{self.colour} {self.name} turned left'
            elif direction_comp.casefold() == 'right':
                return f'{self.colour} {self.name} turned right'
            elif direction_comp.casefold() == 'back':
                return f'{self.colour} {self.name} turned back'

    def show_speed(self):
        return f'{self.colour} {self.name}, current speed is {self.speed} km/h'


class Towncar(Car):

    def __init__(self, speed, colour, name, is_police=False):
        super().__init__(speed, colour, name, is_police)

    def show_speed(self):
        if self.speed <= 60:
            return f'{self.colour} {self.name}, current speed is {self.speed} km/h'
        else:
            return f'{self.colour} {self.name}, speed exceeded'

class Workcar(Car):

    def __init__(self, speed, colour, name, is_police=False):
        super().__init__(speed, colour, name, is_police)

    def show_speed(self):
        if self.speed <= 40:
            return f'{self.colour} {self.name}, current speed is {self.speed} km/h'
        else:
            return f'{self.colour} {self.name}, speed exceeded'


class Sportcar(Car):

    def __init__(self, speed, colour, name, is_police=False):
        super().__init__(speed, colour, name, is_police)


class Policecar(Car):

    def __init__(self, speed, colour, name, is_police=True):
        super().__init__(speed, colour, name, is_police)

car_01 = Towncar(randint(0, 150), 'green', 'Beetle')
print(f'{car_01.colour} {car_01.name}, {car_01.speed}, Is police? {car_01.is_police}')
print(car_01.go())
print(car_01.turn('LeFt'))
print(car_01.show_speed())

car_02 = Workcar(randint(0, 150), 'yellow', 'CAT')
print(f'{car_02.colour} {car_02.name}, {car_02.speed}, Is police? {car_02.is_police}')
print(car_02.go())
print(car_02.turn('back'))
print(car_02.show_speed())

car_03 = Sportcar(randint(0, 150), 'red', 'Jaguar')
print(f'{car_03.colour} {car_03.name}, {car_03.speed}, Is police? {car_03.is_police}')
print(car_03.go())
print(car_03.turn('RIGHT'))
print(car_03.show_speed())

car_04 = Policecar(randint(0, 150), 'yellow', 'Dodge')
print(f'{car_04.colour} {car_04.name}, {car_04.speed}, Is police? {car_04.is_police}')
print(car_04.go())
print(car_04.turn('LeFt'))
print(car_04.turn('RIGHT'))
print(car_04.turn('back'))
print(car_04.show_speed())
# print(car_04.stop())

car_05 = Policecar(0, 'dark_blue', 'Dodge')
print(f'{car_05.colour} {car_05.name}, {car_05.speed}, Is police? {car_05.is_police}')
print(car_05.stop())
