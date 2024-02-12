from django.test import TestCase
from rest_framework.test import APIClient
from .models import Product
from django.urls import reverse

# Create your tests here.
class ProductAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(
            name="Test Product",
            SKU="SKU10100",
            category="Test Category",
            in_stock=True,
            available_stock=100
        )

    def test_retrieve_products(self):
        response = self.client.get(reverse('retrieveProducts'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_product_detail(self):
        response = self.client.get(reverse('retrieveDetail', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], self.product.name)
        # Add a new product and check if it is in the list of products
        
    