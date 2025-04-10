import unittest
from calculator import add, multiply, divide, subtract

class TestCalculator(unittest.TestCase):
    
    def test_add_returns_correct_result(self):
        result = add(12, 5)
        self.assertEqual(result, 17, "Results are not equal")
        
    def test_multiply_returns_correct_result(self):
        result = multiply(3, 5)
        self.assertEqual(result, 15)
        
    def test_divide_returns_correct_result(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)
        
    def test_subtract_returns_correct_result(self):
        result = subtract(15, 7)
        self.assertEqual(result, 8)

