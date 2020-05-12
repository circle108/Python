
# Task 1
age = input('enter your age: ')
name = input('enter your name: ')
surname = input('enter your surname: ')
print(f'Age: {age} Name: {name} Surname: {surname}')


# Task 2

user_time = int(input(' enter seconds pls: '))

hours = user_time // 3600
minutes = (user_time // 60) % 60
seconds = user_time % 60
print(f' h: {hours} m: {minutes} s: {seconds}')

# Task 3

n = input('enter number: ')
print(int(n) + int(n+n) + int(n+n+n))

#Task 4

number = int(input('enter a number: '))
max = 0
n = number
while n:
    if n % 10 > max:
        max = n % 10
    n = n // 10
print(max)

# Task 5

income = int(input('enter profit, usd: '))
cost = int(input('enter coast, usd: '))
if income > cost:
    profit = income - cost
    print('you have an income, usd:', profit)
    print('profitability: ', income / cost)
    n = int(input('Enter the number of employees:'))
    profit_person = profit / n
    print('profit a person: ', profit_person)
else:
    profit = income - cost
    print('you have a loss, usd', profit)

# Task 6
a = 2
b = 3
day = 1
while (b >= a):
    a = a + (a * 0.1)
    day = day + 1
print('день', day, a)



