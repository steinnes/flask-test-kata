from unittest import TestCase
from calculator.logic import Calculator


class CalculatorTests(TestCase):
    def test_mul(self):
        calc = Calculator()
        result = calc.mul(3, 4)
        self.assertEquals(result, 12)

    def test_div(self):
        pass
