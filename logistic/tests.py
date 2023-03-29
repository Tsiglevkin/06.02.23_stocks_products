from django.test import TestCase
from rest_framework.test import APIClient


class TestView(TestCase):
    def test_product_view(self):
        client = APIClient()
        response = client.get('/api/v1/products/')
        self.assertEqual(response.status_code, 200)
