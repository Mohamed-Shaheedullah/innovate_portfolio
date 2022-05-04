import random
# from random import random, randint, uniform


# print to display in terminal
print("current file")

# strings are for representing characters
print("Hello 1234")

# this is an integer
print(1234)

# this is a floating point, any decimal
print(1234.5)

#  booleans - True and False
print(True)
print(False)

# none - a blank, or null type
print(None)


print(len("hello"))

# index position
print("hello"[1])

# last letter
print("hello"[-1])

# upper

print("hello".upper())

# Libraries
# random
print(random.random())
# between 0 and just under 1

print(random.uniform(1,10))
# inclusive

print(random.randint(1, 10))

# print(uniform())

# variables

my_name  = "Raf"

my_age = 56

print(my_name)

print("Hello my name is ", my_name)
print("Hello my name is " + my_name)
# concat only works with strings
print("hello my name is {} and I am {} years old".format(my_name, my_age))
print(f"Hello my name is {my_name } and I am {my_age} years old")

# operators

print(1+2)
print(2-1)
print(2*3)
print(2**3)
print(15%3)

balance = 100
amount = 50

print(balance - amount)
# balance -= amount

balance = balance -amount
print(balance)

# char_name = input("What is your name?")

# print(f"Welcome, {char_name}")
# input is always a string


# conditionals
music = "classical"

if music =="classical":
    print("Oh no classical")
elif music == "pop":
    print("Turn it up")
else:
    print("Yay")


print(10%2 == 0)

num1 = 10
num2 = 20

if num1 > num2:
    print("num1 is bigger")
elif num1 < num2:
    print("num2 is bigger")
else:
    print("num1 and num2 are the same")


# remember sequence matters
num =14
if num%7==0 and num%3==0:
    print("fizzbuzz")
elif num%3 == 0:
    print("fizz")
elif num%7==0:
    print("buzz")


place = "Liverpool"
weather = "Cloudy"

if place == "Liverpool" and weather == "Rainy":
    print("of course")

# functions
def light_switch():
    print("Who turned out the lights?")

light_switch()

def cash_withdrawal(amount, accnum):
    #params
    print(f"Withdrawing {amount} from account {accnum}")

cash_withdrawal(300, 50449921)
#arguments

# Lists
coffee_order=["alex-cortado", "Ben-Latte", "Charlie-Cappucino"]

print(coffee_order)

coffee_order[2] = "new coffee"

print(coffee_order)
coffee_order.append("Donna-espresso")

print(coffee_order)

coffee_order.pop()
# can put index in pop

print(coffee_order)

# loops

drinks = ["coke", "fanta", "tonic"]

for i in drinks:
    print(i)

for i in range(10):
    print(i)
# does not include last number

num10 = 0

while num10 < 10 :
    num10 +=1
    print("num")




