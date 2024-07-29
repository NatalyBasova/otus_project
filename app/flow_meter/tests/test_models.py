from django.test import TestCase
from flow_meter.models import Product


class TestProduct(TestCase):
    def setUp(self):
        Product.objects.create(
            name="pen",
            quantity=12,
        )

    def tearDown(self):
        product = Product.objects.get(name="pen")
        product.delete()

    def test_product_created(self):
        product = Product.objects.get(name="pen")
        self.assertEqual(product.name, "pen")
