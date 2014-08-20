from unittest import TestCase
from flask.testing import FlaskClient


class ViewTests(TestCase):
    def setUp(self):
        from flask import current_app
        self.client = FlaskClient(current_app)

    def test_calculate_multiply_two_positive_numbers(self):
        pass
