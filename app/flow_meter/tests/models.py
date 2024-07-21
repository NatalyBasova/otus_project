from django.test import TestCase
from flow_meter.models import Product


class TestProduct(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="pen",
            quantity=12,
        )

    def tearDown(self):
        print("Я выполняюсь после каждого теста")
