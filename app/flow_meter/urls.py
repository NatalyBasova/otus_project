from django.contrib import admin
from django.urls import path, include


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("products/", views.all_products, name="products"),
    path("products/details/<int:id>", views.product_details, name="product_details"),
    path("products/delete/<int:id>", views.product_delete, name="product_delete"),
    path("products/add", views.add_product, name="add_product"),
    path("about", views.about, name="about"),
]
