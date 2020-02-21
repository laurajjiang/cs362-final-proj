# CS362 Final Project
# Calculator Tests

# Laura Jiang (jianglau)
# Alekos Hovecamp (hovekama)
# Arthur York (yorkar)

import math
import unittest
import sys
import calculator

class TestCalculator(unittest.TestCase):
    def testInit(self):
        calc = calculator.Calculator("degrees")
        self.assertEqual(calc.angle, "degrees")

        calc = calculator.Calculator("radian")
        self.assertEqual(calc.angle, "radian")

    def testMenu(self):
        calc = calculator.Calculator("radian")
        res = calc.menu(1, 5, None)
        self.assertEqual(res, "Value Error")
        res = calc.menu(1, 5, 5)
        self.assertEqual(res, 25)

        res = calc.menu(2, 5, None)
        self.assertEqual(res, "Value Error") 
        res = calc.menu(2, 5, 5)
        self.assertEqual(res, 1)
        res = calc.menu(3, 9)
        self.assertEqual(res, 3)
        res = calc.menu(4, 9)
        self.assertEqual(res, 81)
        res = calc.menu(5, 1)
        self.assertEqual(res, 1)
        res = calc.menu(6, 5)
        self.assertEqual(res, 120)
        res = calc.menu(7, -2)
        self.assertEqual(res, 2)
        res = calc.menu(8, 0)
        self.assertEqual(res, 0)
        res = calc.menu(9, 0)
        self.assertEqual(res, 1)

        res = calc.menu(10, 1)
        self.assertEqual(res, "Error")
        res = calc.menu(-1, 1)
        self.assertEqual(res, "Error")

    def testMultiplication(self):        
        calc = calculator.Calculator("radian")
        product = calc.multiply(0, 45)
        self.assertEqual(product, 0);
        product = calc.multiply(0, -45.2)
        self.assertEqual(product, 0);

        product = calc.multiply(1, sys.maxsize)
        self.assertEqual(product, sys.maxsize)
        product = calc.multiply(1, -sys.maxsize)
        self.assertEqual(product, -sys.maxsize)

        product = calc.multiply(5, 0.5)
        self.assertEqual(product, 2.5)
        product = calc.multiply(1.1, 1.2)
        self.assertEqual(product, 1.32)

    def testDivision(self):
        calc = calculator.Calculator("radian")
        div = calc.divide(1, 0)
        self.assertEqual(div, "Value Error")
        div = calc.divide(1.5, 0)
        self.assertEqual(div, "Value Error")
        div = calc.divide(-1, 0)
        self.assertEqual(div, "Value Error")

        div = calc.divide(45, 9)
        self.assertEqual(div, 5)
        div = calc.divide(-45, 9)
        self.assertEqual(div, -5)

        div = calc.divide(5, 1.0)
        self.assertEqual(div, 5.0)

        div = calc.divide(5.0, 1)
        self.assertEqual(div, 5.0)

        div = calc.divide(sys.maxsize, 1)
        self.assertEqual(format(div, '.0f'), format(sys.maxsize+1, '.0f'))
        div = calc.divide(-sys.maxsize, -1)
        self.assertEqual(format(div, '.0f'), format(sys.maxsize+1, '.0f'))

    def testSqRoot(self):
        calc = calculator.Calculator("radian")
        res = calc.sqRoot(0)
        self.assertEqual(res, 0)
        
        res = calc.sqRoot(-1)
        self.assertEqual(res, "Value Error")
        
        res = calc.sqRoot(100)
        self.assertEqual(res, 10)
        res = calc.sqRoot(2.5)
        self.assertEqual(int(res), 1)
        res = calc.sqRoot(2)
        self.assertEqual(int(res), 1)

        res = calc.sqRoot(6/3)
        self.assertEqual(int(res), 1)
        
    def testSquare(self):
        calc = calculator.Calculator("radian")
        res = calc.square(0)
        self.assertEqual(res, 0)
        
        res = calc.square(1)
        res2 = calc.square(-1)
        self.assertEqual(res, res2)

        res = calc.square(1.1)
        self.assertEqual(round(res, 2), 1.21)
        res = calc.square(99999)
        self.assertEqual(res, 9999800001)
        res = calc.square(-99999)
        self.assertEqual(res, 9999800001)

    def testInverse(self):
        calc = calculator.Calculator("radian")
        res = calc.inverse(0)
        self.assertEqual(res, "Value Error")
        
        res = calc.inverse(1)
        self.assertEqual(res, 1)
        res = calc.inverse(-1)
        self.assertEqual(res, -1)

        res = calc.inverse(1/2)
        res2 = calc.inverse(0.50)
        self.assertEqual(res, res2)
        res = calc.inverse(1.6)
        self.assertEqual(res, 0.625)

    def testFactorial(self):
        calc = calculator.Calculator("radian")
        res = calc.fact(0)
        self.assertEqual(res, 1)
        res = calc.fact(1)
        self.assertEqual(res, 1)
        res = calc.fact(-1)
        self.assertEqual(res, "Value Error")

        res = calc.fact(5)
        self.assertEqual(res, 120)
        res = calc.fact(14)
        self.assertEqual(res, 87178291200)
        res = calc.fact(99)
        self.assertEqual(len(str(res)), 156)

    def testAbsValue(self):
        calc = calculator.Calculator("radian")
        res = calc.absValue(0)
        self.assertEqual(res, 0)
        res = calc.absValue(-1)
        self.assertEqual(res, 1)

        res = calc.absValue(2.5)
        self.assertEqual(res, 2.5)
        res= calc.absValue(-2.5)
        self.assertEqual(res, 2.5)

        res = calc.absValue(sys.maxsize)
        self.assertEqual(format(res, '.0f'), format(sys.maxsize+1, '.0f'))
        res = calc.absValue(-sys.maxsize)
        self.assertEqual(format(res, '.0f'), format(sys.maxsize+1, '.0f'))

    def testSine(self):
        calc = calculator.Calculator("degrees")
        self.assertEqual(calc.angle, "degrees")
        res = calc.sin(0)
        self.assertEqual(res, 0)
        res = calc.sin(15.5)
        self.assertEqual(round(res, 3), 0.267)
        res = calc.sin(90)
        self.assertEqual(res, 1)
        res = calc.sin(45)
        self.assertEqual(round(res, 3), 0.707)
        res = calc.sin(-45)
        self.assertEqual(round(res, 3), -0.707)
        res = calc.sin(1440)
        self.assertEqual(int(res), 0)

        calc = calculator.Calculator("radian")
        self.assertEqual(calc.angle, "radian")
        res = calc.sin(0)
        self.assertEqual(res, 0)
        res = calc.sin(1.12)
        self.assertEqual(round(res, 3), 0.900)
        res = calc.sin(1.57)
        self.assertEqual(round(res, 3), 1)
        res = calc.sin(6.28)
        self.assertEqual(int(res), 0)
        res = calc.sin(-6.28)
        self.assertEqual(int(res), 0)
        res = calc.sin(25.13)
        self.assertEqual(int(res), 0)

    def testCosine(self):
        calc = calculator.Calculator("degrees")
        self.assertEqual(calc.angle, "degrees")
        res = calc.cos(0)
        self.assertEqual(res, 1)
        res = calc.cos(15.1)
        self.assertEqual(round(res, 3), 0.965)
        res = calc.cos(90)
        self.assertEqual(int(res), 0)
        res = calc.cos(45)
        self.assertEqual(round(res, 3), 0.707)
        res = calc.cos(-45)
        self.assertEqual(round(res, 3), 0.707)
        res = calc.cos(1440)
        self.assertEqual(res, 1)

        calc = calculator.Calculator("radian")
        self.assertEqual(calc.angle, "radian")
        res = calc.cos(0)
        self.assertEqual(res, 1)
        res = calc.cos(1.12)
        self.assertEqual(round(res, 5), 0.43568)
        res = calc.cos(1.57)
        self.assertEqual(round(res, 6), 0.000796)
        res = calc.cos(6.28)
        self.assertEqual(math.ceil(res), 1)
        res = calc.cos(-6.28)
        self.assertEqual(math.ceil(res), 1)
        res = calc.cos(25.13)
        self.assertEqual(math.ceil(res), 1)
