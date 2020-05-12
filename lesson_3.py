# Task 1
def division(a, b):
  try:
      print(a / b)
  except ZeroDivisionError:
        print('division by zero is impossible, result = 0')
a = int(input('enter a for a / b:'))
b = int(input('enter b for a / b:'))
division(a,b)
# Task 2
def my_phonebook(name = input('Введите имя:'), surname = input('Введите фамилию:'),
                 adress = input('Введите ваш адрес:'),
                 data = input('Дата рождения:'), email = input('Ваш email: ')):
    print('Имя: {}, Фамиия: {}, Адрес: {}, Дата рождения: {}, Email: {}'.format(name, surname, adress, data, email))

my_phonebook()

# Task 3
def my_func(a, b, c):
    e = min(a, b, c)
    d = a + b + c - e
    print(d)
my_func(8,9,56)

# Task 4
def my_func(x, y):
    c = x**y
    print(c)
my_func(3,-5)

def my_func1(x, y):
    z = 1
    for i in range(abs(y)):
        z *= x
    if y < 0:
        print(1 / z)
    else:
        print(z)

my_func1(3, -5)

# Task 5

total_sum = 0
boba = True
while boba == True:
    number = input('enter:').split()
    sum = 0
    for el in range(len(number)):
        if number[el] =='q':
            boba = False
            break
        else:
            sum+=int(number[el])
    print(f'current sum{sum}')
    total_sum = total_sum + sum
    print(f'total sum {total_sum}')

#Task 6

def int_func(x):
    print(x.title())
int_func('fight')