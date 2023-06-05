name = "Bro Code"

first_name = name[1:3]
last_name = name[4:]
funky_name = name[0:8:2]
reversed_name = name[::-1]

#print(funky_name)
#print(reversed_name)

website = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website[slice])
print(website2[slice])

age = int(input("How old are you?: "))

temp = int(input("What is the temperature outside?: "))
if temp >= 0 and temp <= 30:
    print("the temperature is good today!")
    print("go outside")
elif temp < 0 or temp > 30:
    print("the temperature is bad today!")
    print("stay inside!")

name = None
while not name:
    name = input("Enter your name")

print("Hello "+name)
for i in range(10):
    print(i+1)

for i in range(10):
    print(i+1)

for i in range(50, 100+1, 2):
    print(i)

for i in "Bro Code":
    print(i)

for seconds in range(10, 0, -1):
    print(seconds)
print("Happy New Year!")

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
            print(symbol, end="")
    print()

# Loop Control Statements = change a loops execution from its normal sequence

# break = used to terminate the loop entirely
# continue = skips to the next itreation of the loop
# pass = does nothing, acts as a placeholder

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)

# list = used to store multiple items in a single variable

food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]
print(food) #prints all of the elements in the list

food[0] = "sushi"

food.append("ice-cream")
food.remove("hotdog")
food.pop() #pops the last element
food.insert(0,"cake") # inserts at the given index
food.sort() #sorts the list alphabetically
food.clear() #clears the given list

for x in food:
    print(x)

# 2D lists = a list of lists
drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice-cream"]

food = [drinks, dinner, dessert]

print(food[0][0]) #access coffee from drinks list

# tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("Bro",21,"male")

print(student.count("Bro"))
print(student.index("male"))

for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here:")

# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")
for x in utensils:
    print(x)

print(dishes.difference(dishes))
print(utensils.intersection(dishes))

#dictionary = A changeable, unordered collection of unique key: value pairs
# Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India': 'New Delhi',
            'China':'Bejing', 'Russia':'Moscow'}

capitals.update({'Germany': 'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
capitals.clear()

print(capitals['Russia'])
print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values)
print(capitals.items())

for key,value in capitals.items():
    print(key, value)

# index operator [] = gives access to a sequence's element (str,list,tuples)

name = "bro Code:"

first_name = name[:3].upper()
last_name = name[4:].lower()
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)

name = "bro Code!"

if(name[0].islower()):
    name = name.capitalize()

first_name = name[:3].upper()
last_name = name[4:].lower()
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)

# function = a block of code which is executed only when it is called.

def hello(first_name, last_name, age):
    print("hello "+first_name+" "+last_name)
    print("You are "+str(age)+" years old")
    print("Have a nice day!")

hello("Bro", "Code", 21)

# return statement = Functions send Python values/objects back to the caller.
#                    These values/objects are known as the function's return value

def multiply(number1, number2):
    return number1 * number2

x = multiply(6,8)

print(x)

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

hello(last="Code",middle="Dude",first="Bro")

# keyword arguments = arguments preceded by an identifier when we pass them to a function
#                     The order of the arguments doesn't matter, unlike positional arguments
#                     Python knows the names of the arguments that our function receives

# nested functions calls = functions calls inside other function calls
#                          innermost function calls are resolved first
#                          returned value is used as argument for the next outer function calls

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

print(round(abs(float(input("Enter a whole positive number: ")))))
# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created
#         A global and locally scoped versions of a variable can be created

name = "Bro" # global scope (available inside & outside functions)

def display_name():
    name = "Code" # local scope (available only inside the function)
    print(name)

print(name)

# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments


def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5,6))


def hello(first, last):
    print("Hello " + first + " " + last)

# **kwargs = parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs):
    #print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end=" ")
    for key,value in kwargs.items():
            print(value,end=" ")

hello(title ="Mr.",first="Bro",middle = "Dude",last = "Code")

# str.format() = optional method that gives users
#                more control when displaying output

animal = "cow"
item = "moon"

print("The "+animal+"jumped over the "+item)
print("The {} jumped over the {}".format(animal,item))
print("The {1} jumped over the {0}".format(animal,item)) #positional argument
print("The {} jumped over the {}".format(animal,item)) #keyword argument
print("The {animal} jumped over the {animal}".format(animal="cow",item="moon")) #positional argument

text = "The {} jumped over the {}"
print(text.format(animal,item))

name = "Bro"
print("Hello, my name is {}".format(name))
print("Hello, my name is {0:10}. Nice to meet you".format(name))
print("Hello, my name is {:<10}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name))
print("Hello, my name is {:^10}. Nice to meet you".format(name))

number = 1000

print("The number pi is {:.3f}".format(number))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number)) #Displays number in binary
print("The number is {:o}".format(number)) #Displays number in octal
print("The number is {:x}".format(number)) #Displays number in hexadecimal
print("The number is {:e}".format(number)) #Displays number in scientific notaion

import random

x = random.randint(1,6)
y = random.random()

myList = ['rock','paper','scissors']
z = random.choice(myList) #prints a random choice from myList

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

random.shuffle(cards)

print(cards)

#execution = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
    print(result)
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero: idiot:")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
except Exception as e:
    print(e)
    print("something went wrong :(")
else:
    print(result)
finally:
    print("This will always execute")

import os

path = "C:\\Users\\Cakow\\Desktop\\test.txt"

if os.path.exists(path):
    print("That location exists:")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory:")
else:
    print("That location doesn't exist:")

import os

path = "C:\\Users\\Cakow\\Desktop\\test.txt"

if os.path.exists(path):
    print("That location exists:")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exist:")

try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")

print(file.closed) #prints true if true otherwise false

text = "Yoooooooooo\nThis is some text\nHave a good one!\n"

with open('test.txt','w') as file:
    file.write(text)

text = "Have a nice day! See ya"

#appends to the end of a file
with open('test.txt','a') as file:
    file.write(text)

# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification dates)

import shutil

shutil.copy2('test.txt','copy.txt') #src,dst

import os

source = "test.txt"
destination = "C:\\Users\\Cakow\\Desktop\\test.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")

import os
import shutil
path = "empty_folder"

try:
    os.remove(path)    #delete a file
    #os.rmdir(path)     #deletes an empty directory
    #shutil.rmtree(path)   #delete a directory containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was not deleted")

# module = a file containing python code. Many contain functions, classes, etc.
# used with modular programming, which is to seperate a program into parts

#import messages as msg

#msg.hello()
#msg.bye()

#from messages import hello,bye

#hello()
#bye()

#help("modules") #lists all the modules available to you by python

import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        print("computer: ",computer)
        print(player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print(player)
            print("You lose!")
        if computer == "scissors":
            print("computer: ", computer)
            print(player)
            print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("Bye!")


class Car:

    wheels = 4 #class variable

    def __init__(self, make, model, year, color):
        self.make = make    #instance variable
        self.model = model  #instance variable
        self.year = year    #instance variable
        self.color = color  #instance variable

    def drive(self):
        print("This car is driving")

    def stop(self):
        print("This car is stopped")

#from car import Car
# car_1 = Car("Chevy", "Corvette",2021,"blue")
# car_2 = Car("FOrd", "Mustang", 2022, "red")

#print(car_1.wheels)
#print(car_2.wheels)

# print(car_2.make)
# print(car_2.model)
# print(car_2.year)
# print(car_2.color)

# car_2.drive()
# car_2.stop()

class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def slumber(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")
class Fish(Animal):
    def swim(self):
        print("This fish is swimmming")
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

#print(rabbit.alive)
#fish.eat()
#hawk.sleep()

#multi-level inheritance = when a derived (child) class inherits another derived (child) class

class Organism:

    alive = True

class Animal(Organism):

    def eat(self):
        print("This animal is eating")

class Dog(Animal):
    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.alive)    # inherited from the Organism class
dog.eat()           # inherited from the Animal class
dog.bark()          # defined in Dog class

#----------------------------------------------------------
class Prey:

    def flee(self):
        print("This animal flees")

class Predator:

    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

class Animal:

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):

# method chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print("You start the engine")
        return self
    def drive(self):
        print("You drive the car")
        return self
    def brake(self):
        print("You step on the brakes")
        return self
    def turn_off(self):
        print("You turn off the engine")
        return self

car = Car()
# car.turn_on().drive()

# car.brake().turn_off()

# super() = Function used to give access to the methods of a parent class.
#           Returns a temporary object of a parent class when used

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length,width)

    def area(self):
        return self.length*self.width

class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length,width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height
square = square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())

# Prevents a user from creating an object of that class
# - compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation

class Car:

    color = None

def change_color(car, color):
    car.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

change_color(car_1, "red")
change_color(car_2, "white")
change_color(car_3, "blue")

print(car_1.color)
print(car_2.color)
print(car_3.color)

# Duck typing = concept where the class of an object is less important than the name
#               class type is not checked if minimum methods/attributes are present
#               "If it walks like a duck, and it quacks like a duck, then it must be a duck."
class Duck:

    def walk(self):
        print("This duck is walking")
    def talk(self):
        print("This duck is quacking")

class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person():

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)

foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)

# happy = True
# print(happy)

print(happy := True)

# Higher Order Function = a function that either:
#                         1. accepts a function as an argument
#                              or
#                         2. returns a function
#                         (In python, functions are also treated as objects)

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(10))

# lambda function = function written in 1 line using lambda keyword
#                 accepts any number of arguments, but only has one expression
#                 (think of it as a shortcut)
#                 (useful if needed for a short period of time, throw-away))
#
# lambda parameters: expression

double = lambda x:x*2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name+" "+last_name
age_check = lambda age:True if age >= 18 else False
print(age_check(18))

# sort() method = used with lists
# sort() function = used with iterables

students = [("Squidward", "F", 60)
            ("Sandy", "A", 33)
            ("Patrick", "D", 36)
            ("Spongebob", "B", 20)
            ("Mr.krabs", "C", 78)]

# map() = applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function, iterable)

store = [("shirts",20.00),
         ("pants",25.00),
         ("jacket",50.00)
         ("socks", 10.00)]

to_euros = lambda data: (data[0], data[1] * 0.82)
to_dollars = lambda data: (data[0], data[1]/ 0.82)

store_dollars = list(map(to_euros, store))

for i in store_dollars:
    print(i)

# filter() = creates a collection of elements from an iterable for which a function returns true
#
# filter(function, iterable)

friends = [("Rachel",19),
           ("Monica", 18),
           ("Phoebe",17),
           ("Joey",16),
           ("Chandler",21),
           ("Ross",20)]

age = lambda data:data[1] >= 18

drinking_buddies = list(filter(age, friends))

# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains
#
# reduce(function, iterable)

import functools

letters = ["H", "E", "L", "L", "O"]
word = functools.reduce(lambda x, y,:x + y,letters)
print(word)

factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y,:x * y, factorial)
print(result)

# list comprehension = a way to create a new list with less syntax
#                      can mimic certain lambda functions, easier to read
#                      list = [expression for item in iterabel]
#                      list = [expression for item in iterable if conditional]
#                      list = [expression if/else for item in iterable]

squares = []
for i in range(1, 11):
    squares.append(i * i)
print(squares)

squares = [i * i for i in range(1,11)]
print(squares)

students = [100, 90, 80, 70, 60, 50, 40, 30, 0]

passed_students = list(filter(lambda x: x >= 60, students))
print(passed_students)

# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions
#dictionary = {key: expression for (key,value) in iterable}

cities_in_F = {'New York': 32, 'Boston':75, 'Los Angeles': 100, 'Chicago': 50}

cities_in_C = {key: ((value-32)*(5/9)) for (key,value) in cities_in_F.items()}


cities = {'New York':32, 'Boston':75, 'Los Angeles': 100, 'Chicago':50}
desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}
print(desc_cities)

def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"

# zip(iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                  creates a zip object with paired elements stored in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ["p@ssword", "abc123", "guest"]
login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]

users = zip(usernames, passwords, login_date)

for i in users:
    print(i)

# thread = a flow of execution. Like a seperate order of instructions.
#               However each thread takes a turn running to achieve concurrency
#               GIL = (global interpreter lock),
#               allows only one thread to hold the control of the Python interpreter

# cpu bound = program/task spends most of it's time waiting for internal events

# io bound = program/task spends most of it's time waiting for external events

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drank coffee")

def study():
    time.sleep(5)
    print("You finish studying")

x = threading.Thread(target =eat_breakfast(), args=())
x.start()

y = threading.Thread(target =drink_coffee(), args=())
y.start()

z = threading.Thread(target =study(), args=())
z.start()

eat_breakfast()
drink_coffee()
study()

print(threading.active_Count())
print(threading.enumerate())
print(time.perf_counter())

# daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exciting
#                 non-daemon threads cannot normally be killed, stay alive until task is complete
#
#

import threading
import time

def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for:", count, "seconds")

x = threading.thread(target=timer, daemon=True)
x.start()

x.setDaemon(True)

answer = input("Do you wish to exit?")

# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count =0
    while count < num:
        count += 1

def main():

    a = Process(target=counter, args = (500000))
    b = Process(target=counter, args = (500000))
    c = Process(target=counter, args=(500000))
    d = Process(target=counter, args=(500000))

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()



























