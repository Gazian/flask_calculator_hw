import unittest
from modules.calculator import *

class TestCalculator(unittest.TestCase):

    def test_calc_add_function(self):
        sum = calc_add_function(2,3)
        self.assertEqual(5,sum)

    def test_calc_subtract_function(self):
        sum = calc_subtract_function(5,3)
        self.assertEqual(2,sum)

    def test_calc_multiply_function(self):
        sum = calc_multiply_function(2,3)
        self.assertEqual(6,sum)

    def test_calc_divide_function(self):
        sum = calc_divide_function(9,3)
        self.assertEqual(3,sum)