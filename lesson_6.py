# Task 1

from time import sleep
class TrafficLight:
    _color = ['red','yellow','green']
    def running(self):
        while True:
            for el in TrafficLight._color:
                if el == 'red':
                    print(el)
                    sleep(7)
                elif el == 'yellow':
                    print(el)
                    sleep(5)
                elif el == 'green':
                    print(el)
                    sleep(3)
traffic = TrafficLight()
traffic.running()

# Task 2

class Road:
    def __init__(self, lentgh, width):
        self._lentgh = lentgh
        self._width = width
    def asphalt(self):
        self.weight = 25
        self.thickness = 0.05
        asphalt = self.weight*self._lentgh*self._width*self.thickness/1000
        print(f'You need {asphalt} tons')

roadmap = Road(5000,20)
roadmap.asphalt()

# Task 3

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'Name: {self.name}\nSurname: {self.surname}'

    def get_total_income(self):
        total_income = self._income.get('wage')+self._income.get('bonus')
        return f'Income: {total_income}'

a = Position('Donald', 'Duck','Billionaire',300,400)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())

# Task 4
class Car:
    def __init__(self,  speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f'Car went'
    def stop(self):
        return f'Car stopped'
    def turn(self,direction):
        return f'Car turned to {direction}'
    def show_speed(self):
        return f'Your current speed {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


    def show_speed(self):
        if self.speed > 60: return f'You have exceeded the speed limit of 60'

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed,color, name)

    def show_speed(self):
        if self.speed > 40: return f'You have exceeded the speed limit of 40'

ford = TownCar(100,'red' ,'mustang')
bmw = Car(100, 'green', 'exploer', False)
print(ford.show_speed())
print(bmw.show_speed())
print(bmw.turn('right'))
print(bmw.go())
print(bmw.stop())

# Task 5

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f'Start of draw the {title}'

class Pen(Stationery):
    def __init__(self,title):
        super().__init__(title)
    def draw(self):
        return f' {self.title} is drawing with a pen'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f' {self.title} is drawing with a pencil'

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f' {self.title} is drawing with a handle'

picture = Pen('picture')
nature = Handle('nature')
print(picture.draw())
print(nature.draw())
