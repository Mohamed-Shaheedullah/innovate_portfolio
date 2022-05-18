#

class Car():

    color = "red"
    make = "tesla"
    doors = 5
    velocity = 0

    def accelerate():
        velocity += 5

        def stop():
            velocity = 0

wills_car = Car()
wills_car.make = "VW"
