import pytest
from unittest import TestCase
from calculator.logic import Calculator, ValueTooLowException, ValueTooHighException


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

    def test_mul_raises_too_low_exception_on_a_too_low(self):
        calc = Calculator(100, 1000)
        with pytest.raises(ValueTooLowException):
            calc.mul(1, 101)

    def test_mul_raises_too_low_exception_on_b_too_low(self):
        calc = Calculator(100, 1000)
        with pytest.raises(ValueTooLowException):
            calc.mul(101, 1)

    def test_mul_raises_too_high_exception_on_a_too_high(self):
        calc = Calculator(1, 10)
        with pytest.raises(ValueTooHighException):
            calc.mul(11, 5)

    def test_mul_raises_too_high_exception_on_b_too_high(self):
        calc = Calculator(1, 10)
        with pytest.raises(ValueTooHighException):
            calc.mul(5, 11)

    def test_div(self):
        pass
