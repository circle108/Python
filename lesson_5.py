# Task 1
file_name = input('Enter a file`s name: ')
f = open(file_name,'w')
while True:
    text = input('enter text:\n ')
    if text == '': break
    f.write(text+'\n')
f.close()
with open(file_name) as f:
    for line in f:
        print(line, end = '')

# Task 2

my_list = ['Good\n', 'Evening\n']
with open("text1.txt", 'w+') as f:
    f.writelines(my_list)
with open("text1.txt") as f:
    lines = 0
    letters = 0
    for line in f:
        lines += line.count("\n")
        letters = len(line)-1
    print(f"{letters} letters in line")
    print(f"{lines} strings in the text")

# Task 3
llc = {'Gordon': 19000, 'Putin': 21000, 'Tramp': 12000, 'Si': 14000}
try:
    f_obj = open("text3.txt", 'w')
    for last_name, salary in llc.items():
        f_obj.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("input / output error")
finally:
    f_obj.close()
income = 0
count = 0
persons = []
with open("text3.txt") as f_obj:
    for line in f_obj:
        print(line, end="")
        money = line.split(':')
        if int(money[1]) <= 20000:
            persons.append(money[0])
        income += int(money[1])
        count += 1
result = income / count
print(f"persons income less 20000: {persons}")
print(f"average income: {result}")

# Task 4

translate = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
my_list = []
result = []
f_obj = open("text4.txt", 'r')
for line in f_obj:
    content = line.split(" - ")
    print(content)
    if content[0] in translate:
        word = translate[content[0]]
        result.append(word +' - '+ content[1])
print(result)
f_obj.close()
f_input = open("text5.txt", "w")
f_input.writelines(result)
f_input.close()

# Task 5
try:
    with open('text6.txt', 'w+') as f_obj:
        line = input('enter a number: \n')
        f_obj.writelines(line)
        my_num = line.split()
        print(sum(map(int, my_num)))
except IOError:
    print('error in the file')
except ValueError:
    print('input\output error')

# Task 6
