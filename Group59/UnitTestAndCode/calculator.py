# CS362 Final Project
# Calculator 

# Laura Jiang (jianglau)
# Alekos Hovekamp (hovekama)
# Arthur York (yorkar)

import math

class Calculator:
    def __init__(self, angle):
        self.angle = angle

    def menu(self, option, x, y=None):
        if option == 1:
            if y == None:
                return "Value Error"
            return self.multiply(x, y)
        elif option == 2:
            if y == None:
                return "Value Error"
            return self.divide(x, y)
        elif option == 3:
            return self.sqRoot(x)
        elif option == 4:
            return self.square(x)
        elif option == 5:
            return self.inverse(x)
        elif option == 6:
            return self.fact(x)
        elif option == 7:
            return self.absValue(x)
        elif option == 8:
            return self.sin(x)
        elif option == 9:
            return self.cos(x)
        else:
            return "Error"


    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Value Error"
        return x / y

    def sqRoot(self, x):
        if x < 0:
            return "Value Error"
        return math.sqrt(x)

    def square(self, x):
        return x ** 2

    def inverse(self, x):
        if x == 0:
            return "Value Error"
        return 1 / x

    def fact(self, x):
        if x < 0:
            return "Value Error"
        return math.factorial(x)

    def absValue(self, x):
        return math.fabs(x)

    def sin(self, x):
        if self.angle == "degrees":
            x = math.radians(x)
        return math.sin(x)

    def cos(self, x):
        if self.angle == "degrees":
            x = math.radians(x)
        return math.cos(x)

