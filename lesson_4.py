# Task 1

def sal():
    try:
        time = float(input('Выработка часах: '))
        salary = int(input('Ставка USD: '))
        bonus = int(input('Премия в USD: '))
        res = time * salary + bonus
        print(f'заработная плата сотрудника  {res}')
    except ValueError:
        return print('Not a number')
sal()

# Task 2

my_list = [8, 9, 10, 4, 3, 3, 4, 12]
new_list = [el*el for num, el in enumerate(my_list)]
print(f'Current list {my_list}')
print(f'New list {new_list}')

# Task 3

print(f'чисел в пределах от 20 до 240 найти числа, кратные 20 или 21 {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

# Task 4

my_list = [2, 6, 6, 3, 4, 5, 7, 6, 12, 6]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)

# Task 5

from functools import reduce
def my_func(el_p, el):
    return el_p * el
print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'результат вычисления произведения всех элементов списка {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')

# Task 6

from itertools import count
for el in count(int(input('Enter a first number: '))):
    print(el)
from itertools import cycle
my_list = [True, 'ABC', 123, None]
for el in cycle(my_list):
    print(el)

# Task 7

from itertools import count
from math import factorial

def my_gen():
    for el in count(1):
        yield factorial(el)
gen = my_gen()
x = 0
for i in gen:
    if x < 15:
        print(i)
        x += 1
    else:
        break

