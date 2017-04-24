import pytest
from unittest import TestCase

from calculator.logic import Calculator, ValueTooLowException, ValueTooHighException


class CalculatorTests(TestCase):
    def setUp(self):
        self.calc = Calculator(1, 10)

    def test_mul(self):
        assert self.calc.mul(6, 5) == 30

    def test_mul_with_two_positive_numbers(self):
        assert self.calc.mul(6, 5) == 30

    def test_mul_with_two_negative_numbers(self):
        calc = Calculator(-10, 10)
        assert calc.mul(-1, -1) == 1

    def test_mul_with_one_negative_one_positive_number(self):
        calc = Calculator(-10, 10)
        assert calc.mul(-1, 1) == -1

    def test_mul_with_first_value_too_low(self):
        with pytest.raises(ValueTooLowException):
            calc = Calculator(1, 10)
            calc.mul(0, 2)

    def test_mul_with_first_value_too_high(self):
        with pytest.raises(ValueTooHighException):
            calc = Calculator(1, 10)
            calc.mul(11, 2)

    def test_mul_with_second_value_too_low(self):
        with pytest.raises(ValueTooLowException):
            calc = Calculator(1, 10)
            calc.mul(2, 0)

    def test_mul_with_second_value_too_high(self):
        with pytest.raises(ValueTooHighException):
            calc = Calculator(1, 10)
            calc.mul(2, 11)

    def test_mul_first_boundary(self):
        calc = Calculator(1, 10)
        assert calc.mul(1, 9) == 9

    def test_mul_second_boundary(self):
        calc = Calculator(1, 10)
        assert calc.mul(1, 10) == 10

    def test_div(self):
        assert self.calc.div(10, 2) == 5

    def test_div_with_two_positive_numbers(self):
        assert self.calc.div(6, 2) == 3

    def test_div_with_two_negative_numbers(self):
        calc = Calculator(-10, 10)
        assert calc.div(-1, -1) == 1

    def test_div_with_one_negative_one_positive_number(self):
        calc = Calculator(-10, 10)
        assert calc.div(-1, 1) == -1

    def test_div_with_first_value_too_low(self):
        with pytest.raises(ValueTooLowException):
            calc = Calculator(1, 10)
            calc.div(0, 2)

    def test_div_with_first_value_too_high(self):
        with pytest.raises(ValueTooHighException):
            calc = Calculator(1, 10)
            calc.div(11, 2)

    def test_div_with_second_value_too_low(self):
        with pytest.raises(ValueTooLowException):
            calc = Calculator(1, 10)
            calc.div(2, 0)

    def test_div_with_second_value_too_high(self):
        with pytest.raises(ValueTooHighException):
            calc = Calculator(1, 10)
            calc.div(2, 11)

    def test_div_first_boundary(self):
        calc = Calculator(1, 10)
        assert calc.div(1, 1) == 1

    def test_div_second_boundary(self):
        calc = Calculator(1, 10)
        assert calc.div(10, 10) == 1
