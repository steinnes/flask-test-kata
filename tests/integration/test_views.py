from unittest import TestCase
from ..base import TestClient
from calculator.app import app


class ViewTests(TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = TestClient(app)

    def test_multiply_returns_ok(self):
        r = self.client.get("/calc/3*10")
        self.assertEquals(r.status_code, 200)
        self.assertEquals(r.body, "30")

    def test_multiply_returns_403_for_out_of_lower_bound(self):
        r = self.client.get("/calc/-2000*10")
        self.assertEquals(r.status_code, 403)

    def test_multiply_returns_403_for_out_of_upper_bound(self):
        r = self.client.get("/calc/10*2000")
        self.assertEquals(r.status_code, 403)

    def test_divide_returns_ok(self):
        r = self.client.get("/calc/9/3")
        self.assertEquals(r.status_code, 200)
        self.assertEquals(r.body, "3.0")

    def test_divide_returns_403_for_out_of_lower_bound(self):
        r = self.client.get("/calc/-2000/10")
        self.assertEquals(r.status_code, 403)

    def test_divide_returns_403_for_out_of_upper_bound(self):
        r = self.client.get("/calc/10/2000")
        self.assertEquals(r.status_code, 403)
