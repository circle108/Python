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