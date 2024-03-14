import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(10, 5), 15)
        self.assertAlmostEqual(Calculator.add(1.7, 5.9), 7.6, 2)
        self.assertEqual(Calculator.add(-10, 15), 5)
        self.assertEqual(Calculator.add(-10, -15), -25)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(10, 5), 5)
        self.assertAlmostEqual(Calculator.subtract(1.7, 5.9), -4.2, 2)
        self.assertEqual(Calculator.subtract(-10, 15), -25)
        self.assertEqual(Calculator.subtract(-10, -15), 5)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(10, 5), 50)
        self.assertAlmostEqual(Calculator.multiply(1.7, 5.9), 10.03, 2)
        self.assertEqual(Calculator.multiply(-10, 15), -150)
        self.assertEqual(Calculator.multiply(-10, -15), 150)

    def test_divide(self):
        self.assertEqual(Calculator.divide(10, 5), 2)
        self.assertAlmostEqual(Calculator.divide(1.7, 5.9), 0.2881355932203, 2)
        self.assertEqual(Calculator.divide(-10, 15), -0.6666666666666666)
        self.assertEqual(Calculator.divide(-10, -15), 0.6666666666666666)

if __name__ == '__main__':
    unittest.main()