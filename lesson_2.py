# Task 1

myint = 2
mystr = 'Hello Alex'
myfloat = 57.8
mylist = [8, 9, 9]
mytuple = ('h', 8)
mydict = {'name' : 'alex', 'surname' : 'pleshkov'}
general =[myint, mystr, myfloat, mylist, mytuple, mydict]
for i in general:
    print(type(i))

# Task 2
elcount = int(input("enter a count of value: "))
mylist = []
i = 0
el = 0
while i < elcount:
    mylist.append(input("enter nex value: "))
    i += 1
for elem in range(int(len(mylist)/2)):
        mylist[el], mylist[el + 1] = mylist [el + 1], mylist[el]
        el += 2
print(mylist)

# Task 3
seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input("enter a number of year: "))
if month in range(1, 3) or month == 12:
        print(seasons_dict.get(1))
        print(seasons_list[0])
elif month in range(3, 6):
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month in range(6, 9):
    print(seasons_dict.get(3))
    print(seasons_list[2])

elif month in range(9, 12):
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
    print("this month is none")

# Task 4
mystr = input("enter a string: ")
myword = []
num = 0
myword = mystr.split()
for i in myword:
    if len(i) <= 10:
        num+ = 1
        print(num, i)
    else:
        num+ = 1
        print(num, i[0:11])
# Task 5

mylist = [7, 5, 3, 3, 2]
print(mylist)
num = int(input('enter a number: '))
for el in range(len(mylist)):
    if el == num:
        mylist.insert(el + 1, num)
        break
    elif mylist[0] < num:
        mylist.insert(0, num)
        break
    elif mylist[-1] > num:
        mylist.append(num)
        break
    elif mylist[el] > num and mylist[el + 1] < num:
        mylist.insert(el + 1, num)
        break
print(mylist)

# Task 6
goods = int(input("enter quantity of goods: "))
n = 1
mydict = []
mylist = []
myanalys = {}
while n <= goods:
    mydict = dict({'product name:': input("enter name: "), 'price': input("enter price: "),
                    'quantity:': input('enter quantity: '), 'unit': input("enter Unit: ")})
    mylist.append((n, mydict))
    myanalys = dict(
        {'product name:': mydict.get('product name:'), 'price': mydict.get('price'), 'quantity': mydict.get('quantity'),
         'unit': mydict.get('unit')})
    n += 1
for i in mylist:
    print(i)
print(myanalys)