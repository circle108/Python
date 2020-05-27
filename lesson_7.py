# Task 1

class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2
        self.array = [[0,0,0],
                      [0,0,0],
                      [0,0,0]]

    def __add__(self):
        for i in range(len(self.list_1)):
            for j in range(len(self.list_2)):
                self.array[i][j] = self.list_1[i][j] + self.list_2[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.array]))
    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.array]))

my_matrix = Matrix([[1,2,3],
                    [4,5,6],
                    [7,8,9]],
                   [[3,4,5],
                    [6,7,8],
                    [8,7,6]])
print(my_matrix.__add__())

# Task 2

from abc import ABC, abstractmethod
class MyAbstractClass(ABC):
    @abstractmethod
    def get_sqare_coat(self):
        pass
    @abstractmethod
    def get_sqare_jacket(self):
        pass

class Textil(MyAbstractClass):
    def __init__(self,height, width):
        self.height = height
        self.width = width
    def get_sqare_coat(self):
        return self.width / 6.5 + 0.5
    def get_sqare_jacket(self):
        return self.height * 2 + 0.3
    @property
    def get_total_sqare(self):
        return (f'Total sqare of textil: {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')
class Coat(Textil):
    def __str__(self):
        return f'sqare of coat: {self.width / 6.5 + 0.5}'
class Jacket(Textil):
    def __str__(self):
        return f'sqare of coat: {self.height*2 + 0.3}'

textil = Textil(30,80)
coat = Coat(10,20)
jacket = Jacket(88,99)
print(coat)
print(coat.get_total_sqare)
print(textil.get_total_sqare)
print(jacket.get_sqare_jacket())

# Task 3

class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)
    def __str__(self):
        return f'Result {self.quantity * "*"}'
    def __add__(self, other):
        return Cell(self.quantity + other.quantity)
    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Difference is less than 0!')
    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))
    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

cells_1 = Cell(22)
cells_2 = Cell(44)
print(cells_1)
print(cells_2)
print(cells_1 + cells_2)
print(cells_2 - cells_1)
print(cells_1 / cells_2)