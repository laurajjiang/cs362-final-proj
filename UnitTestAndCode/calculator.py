# CS362 Final Project
# Calculator 

# Laura Jiang (jianglau)
# Alekos Hovekamp (hovekama)
# Arthur York (yorkar)

import math

class Calculator:
    def __init__(self, angle):
        self.angle = angle

    def menu(self, option, x, y):
        if option == 1:
            if y == None:
                return "Value Error"
            return multiply(x, y)
        if option == 2:
            if y == None:
                return "Value Error"
            return divide(x, y)
        if option == 3:
            return sqRoot(x)
        if option == 4:
            return square(x)
        if option == 5:
            return inverse(x)
        if option == 6:
            return fact(x)
        if option == 7:
            return absValue(x)
        if option == 8:
            return sin(x)
        if option == 9:
            return cos(x)

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Value Error"
        return x / y

    def sqRoot(self, x):
        return math.sqrt(x)

    def square(self, x):
        return x ** 2

    def inverse(self, x):
        return 1 / x

    def fact(self, x):
        if x < 0:
            return "Value Error"
        return math.factorial(x)

    def absValue(self, x):
        return math.fabs(x)

    def sin(self, x):
        return math.sin(x)

    def cos(self, x):
        return math.cos(x)

