#
#
#

# class Car():
#     def __init__(self, top_speed, weight, engine_format):
#         self.top_speed = top_speed
#         self.weight = weight
#         self.engine_format = engine_format

#     def accelerate(self):
#         print(f"We are accelerating up to {self.top_speed}!")

#     def engine_check(self):
#         print(f"I can see that this engine is a {self.engine_format}.")


# Geoffreys_Car = Car(230, "1.8 tons", "V8")

# Geoffreys_Car.accelerate()
# Geoffreys_Car.engine_check()


class Person():
    def __init__(self, name, age, height): # sets attributes
        self.name= name
        self.height = height
        self.age = age
    def talk(self):
        print(f"Hello my name is {self.name}, I am {self.age} years old")

Will = Person( "Will", 31, "180" )  # values of attributes

print(Will.name)
print(Will.age)
print(Will.height)

Will.talk()

def set_hair(self, hair):
    self.hair =hair

def get_hair(self):
    print(self.hair)

