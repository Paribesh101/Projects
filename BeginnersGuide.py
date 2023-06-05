full_name = 'John Smith'
age = 20
is_new = True
age = input("What is your age? ")
favorite_color = input('What is your favorite color?')
print(age)

weight_lbs = input('Weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)

course = '''
Hi John,

Here is our first email to you.

Thank you,
The support team

'''
print(course)
course = 'Python for Beginners'
print(course[0:3])

name = 'Jennifer'

first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(msg)

course = 'Python for Beginners'
print(len(course))
course.upper()
print(course.upper())
print(course.lower())
print(course)
print(course.find('Beginners'))
print(course.replace('Beginners','Absolute Beginners'))

print(10 ** 3) # 10^3 = 1000

import math

print(math.ceil(2.9))
x = 2.9
print(abs(-2.9))

is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")

print("Enjoy your day")

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")

has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")

weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")

i = 1
while i <= 5:
    print('*' * i)
    i += 1
print("Done")

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')

else:
    print('Sorry, you failed!')

command = ""
started = False
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand")

for item in ['Mosh', 'John', 'Sarah']:
    print(item)

for item in range(5, 10, 2):
    print(item)

numbers = [5, 2, 5, 2, 2]
for item in numbers:
    print('X' * item)

# Finding the largest number in a list
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)

numbers = [5, 2, 1, 7, 4]
number.remove(5)
numbers.insert(0, 10)
numbers.clear()
numbers.pop()
print(numbers)
print(numbers.count(5))
numbers.sort()
numbers.reverse()

numbers = [2, 2, 3, 5, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)

numbers = (1, 2, 3)
numbers[0] = 10
print(numbers[0])

coordinates = (1, 2, 3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

x, y, z = coordinates

coordinates = [1, 2, 3]
x, y, z, = coordinates
print(y)

customer = {
    "name": "John Smith",
    "age": 30,
    "age": 40
    "is_verified": True
}
customer["birthdate"] = "Jan 1 1980"
print(customer["birthdate"])

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "

class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

class Person:
    def __int__(self, name):
        self.name = name

    def talk(self):
        print("talk")

john = Person()
john.talk()











