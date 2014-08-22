# encoding=utf-8


class ValueTooLowException(Exception):
    pass


class ValueTooHighException(Exception):
    pass


class Calculator(object):
    def __init__(self, min_value=-1000, max_value=1000):
        self.min_value = min_value
        self.max_value = max_value

    def _protect_boundaries(self, a, b):
        if a > self.max_value:
            raise ValueTooHighException("Input {} larger than maximum allowed: {}".format(a, self.max_value))
        if a < self.min_value:
            raise ValueTooLowException("Input {} smaller than minimum allowed: {}".format(a, self.max_value))
        if b > self.max_value:
            raise ValueTooHighException("Input {} larger than maximum allowed: {}".format(b, self.max_value))
        if b < self.min_value:
            raise ValueTooLowException("Input {} smaller than minimum allowed: {}".format(b, self.max_value))

    def mul(self, a, b):
        self._protect_boundaries(a, b)
        return a * b

    def div(self, a, b):
        self._protect_boundaries(a, b)
        return float(a) / float(b);
