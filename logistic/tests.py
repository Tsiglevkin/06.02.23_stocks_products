from django.test import TestCase
from rest_framework.test import APIClient, APITestCase

from logistic.models import Stock
from stocks_products.settings import REST_FRAMEWORK


answer = {
    "id": 1,
    "title": "Помидор",
    "description": "Самые сочные и ароматные помидорки"
}


class TestView(TestCase):
    def test_product_view(self):
        client = APIClient()
        response = client.get('api/v1/products/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Stock.objects.get('id'), 1)

# второй вариант через APITestCase

# class TestView(APITestCase):
#     def test_product_view(self):
#         url = 'api/v1/products/1/'
#         response = self.client.get(url)
#         self.assertEqual(response.status_code == 200)


