from unittest import TestCase
from calculator.logic import Calculator


class CalculatorTests(TestCase):
    def test_mul_with_two_positive_numbers(self):
        calc = Calculator()
        result = calc.mul(3, 4)
        self.assertEquals(result, 12)
        
    def test_mul_with_two_negative_numbers(self):
        calc = Calculator()
        result = calc.mul(-3, -4)
        self.assertEquals(result, 12)

    def test_mul_with_one_negative_one_positive_number(self):
        calc = Calculator()
        result = calc.mul(-3, 4)
        self.assertEquals(result, -12)

    def test_div(self):
        pass
