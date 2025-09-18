import unittest
from calculator.calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    
    # Addition tests
    def test_add_positive_numbers(self):
        self.assertEqual(add(3, 5), 8)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add(-3, -5), -8)
    
    # Subtraction tests
    def test_subtract_numbers(self):
        self.assertEqual(subtract(10, 4), 6)
    
    def test_subtract_negative(self):
        self.assertEqual(subtract(-3, -7), 4)
    
    # Multiplication tests
    def test_multiply_numbers(self):
        self.assertEqual(multiply(3, 4), 12)
    
    def test_multiply_with_zero(self):
        self.assertEqual(multiply(5, 0), 0)
    
    # Division tests
    def test_divide_numbers(self):
        self.assertEqual(divide(10, 2), 5)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)
    
    # Edge case tests
    def test_add_float_numbers(self):
        self.assertAlmostEqual(add(2.5, 3.1), 5.6)
    
    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-10, -2), 5)

if __name__ == "__main__":
    unittest.main()
