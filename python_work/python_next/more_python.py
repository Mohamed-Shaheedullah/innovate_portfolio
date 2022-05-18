
# casting
print("this is my file")
print(int(5.4))
print(int("54"))
print(float(54))
print(type(str(54)))

# truthy and falsy

# print("what is your name")
# name = input()

# if name:
#     print(f"Hello {name}")
# else:
#     print("No name")


print(not True)
print(not False)

bool = False
if bool != True:
    print(False)
else:
    print(True)

bool = False
if not bool:
    print(False)
else:
    print(True)



# def add_up():
#     num1 = input("number_1  ")
#     num2 = input("number_2  ")

#     try:
#         print(f"{num1} +{num2} is {int(num1) + int(num2)}")

#     except:
#         print("Error!")
#         print("********************************")
#         add_up()

#     #print(int(num1)+int(num2))

# add_up()


light = False
# global variable, cannot be accesed in functions unless 'global' specified inside function


def light_switch():
    # if put light=false here will always be false, so cannot
    global light
    if light:
        print("Bright")
        light = False
    else:
        print("dark")
        light = True

light_switch()
light_switch()

list1 = ["e1", "e2", "e3"]

tuple1 = (1, 2, 3)

print(list1)
print(tuple1)

even_nums = [2,4,6,8,10]

odd_nums = (1,3,5,7,9)

even_nums.append(12)

even_nums.insert(0,0) # first 0 is index num, second 0 is object to be inserted

print(even_nums)

# odd_nums.remove(1) # not possible for tuples

odd_nums += (11,13,5) # 'can add to a tuple' 

print(odd_nums)

# tuples good for constants

# slicing, start pos, desired end pos + 1
# third number can be step


num10 = 0
while num10 < 10:
    print(num10)
    num10 += 1

# can use 'in' operator for lists
