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

    def test_protect_boundaries_on_a_too_low(self):
        calc = Calculator(100, 1000)
        with pytest.raises(ValueTooLowException):
            calc._protect_boundaries(1, 101)

    def test_protect_boundaries_on_b_too_low(self):
        calc = Calculator(100, 1000)
        with pytest.raises(ValueTooLowException):
            calc._protect_boundaries(101, 1)

    def test_protect_boundaries_on_a_too_high(self):
        calc = Calculator(1, 10)
        with pytest.raises(ValueTooHighException):
            calc._protect_boundaries(11, 5)

    def test_protect_boundaries_on_b_too_high(self):
        calc = Calculator(1, 10)
        with pytest.raises(ValueTooHighException):
            calc._protect_boundaries(5, 11)

    def test_mul_does_not_raise_exception_on_a_on_boundaries(self):
        calc = Calculator(1, 10)
        # test lower bound
        result = calc.mul(1, 5)
        self.assertEquals(result, 5)

        # test upper bound
        result = calc.mul(10, 5)
        self.assertEquals(result, 50)

    def test_mul_does_not_raise_exception_on_b_on_boundaries(self):
        calc = Calculator(1, 10)
        # test lower bound
        result = calc.mul(5, 1)
        self.assertEquals(result, 5)

        # test upper bound
        result = calc.mul(5, 10)
        self.assertEquals(result, 50)

    def test_div_with_two_positive_numbers(self):
        calc = Calculator()
        result = calc.div(12, 3)
        self.assertEquals(result, 4)
        
    def test_div_with_two_negative_numbers(self):
        calc = Calculator()
        result = calc.div(-12, -3)
        self.assertEquals(result, 4)

    def test_div_with_one_negative_one_positive_number(self):
        calc = Calculator()
        result = calc.div(-12, 3)
        self.assertEquals(result, -4)


    def test_div_does_not_raise_exception_on_a_on_boundaries(self):
        calc = Calculator(1, 10)

        # test lower bound
        result = calc.div(1, 2)
        self.assertEquals(result, 0.5)

        # test upper bound
        result = calc.div(10, 5)
        self.assertEquals(result, 2)

    def test_div_does_not_raise_exception_on_b_on_boundaries(self):
        calc = Calculator(2, 10)

        # test lower bound
        result = calc.div(10, 2)
        self.assertEquals(result, 5)

        # test upper bound
        result = calc.div(5, 10)
        self.assertEquals(result, 0.5)

