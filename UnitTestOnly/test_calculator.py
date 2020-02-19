# CS362 Final Project
# Calculator Tests

# Laura Jiang (jianglau)
# Alekos Hovecamp (hovekama)
# Arthur York (yorkar)

import unittest 
import calculator as calc

class TestCalculator(unittest.TestCase):
    def testMultiplication(self):
        product = calc.multiply(0, 45)
        self.assertEqual(product, 0);
        product = calc.multiply(0, -45.2)
        self.assertEqual(product, 0);

        product = calc.multiply(1, math.inf)
        self.assertEqual(product, math.inf)
        product = calc.multiply(1, -math.inf)
        self.assertEqual(product, -math.inf)

        product = calc.multiply(5, 0.5)
        self.assertEqual(product, 2.5)
        product = calc.multiply(1.1, 1.2)
        self.assertEqual(product, 1.32)

    def testDivision(self):
        div = calc.divide(1, 0)
        self.assertEqual(div, 0)
        div = calc.divide(1.5, 0)
        self.assertEqual(div, 0)
        div = calc.divide(-1, 0)
        self.assertEqual(div, 0)

        div = calc.divide(45, 9)
        self.assertEqual(div, 5)
        self.assertEqual(div, 5*9)
        div = calc.divide(-45, 9)
        self.assertEqual(div, -5)
        self.assertEqual(div, -5 * 9)

        div = calc.divide(5, 1.0)
        self.assertEqual(div, 5.0)

        div = calc.divide(5.0, 1)
        self.assertEqual(div, 5.0) 

    def testSqRoot(self):
        res = calc.sqRoot

    def testSquare(self):
        pass

    def testInverse(self):
        pass

    def testFactorial(self):
        pass

    def testAbsValue(self):
        pass

    def testSine(self):
        pass

    def testCosine(self):
        pass
