from django.test import TestCase
from flow_meter.models import Product
from django.urls import reverse


class ProductListViewTest(TestCase):

    def setUp(self):
        number_of_products = 25
        for product_id in range(number_of_products):
            Product.objects.create(
                name="Product {0}".format(product_id), quantity=product_id
            )

    def test_all_products_200(self):
        response = self.client.get("/products/?page=1")
        self.assertEqual(response.status_code, 200)

    def test_products_pagination_is_ten(self):
        response = self.client.get(reverse("products"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context_data)
        self.assertTrue(response.context_data["is_paginated"] is True)
        self.assertEqual(len(response.context_data["object_list"]), 10)
