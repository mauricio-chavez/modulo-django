"""Products app product views test"""

from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APIRequestFactory, APIClient

from ..models import Product


class ProductTest(TestCase):
    """Contains unit and integration tests for products"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='test', password='test', email='test@bedu.org'
        )
        response = self.client.post(
            '/api/token/', {'username': 'test', 'password': 'test'}
        )
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + response.data['access']
        )

    def test_list_view(self):
        """Tests that contains my products"""
        Product.objects.create(name='producto', price=10,
                               rating=5, user=self.user)
        Product.objects.create(name='producto', price=10,
                               rating=5, user=self.user)

        response = self.client.get('/api/product/')

        self.assertEqual(len(response.data), 2)

    def test_list_view_2(self):
        """Tests that contains my products"""
        Product.objects.create(name='producto', price=10,
                               rating=5, user=self.user)
        Product.objects.create(name='producto1', price=102,
                               rating=5, user=self.user)
        Product.objects.create(name='producto2', price=103,
                               rating=5, user=self.user)

        response = self.client.get('/api/product/')

        self.assertEqual(len(response.data), 3)
