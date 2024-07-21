from django.contrib import admin
from django.urls import path, include


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("products/", views.all_products, name="products"),
    path("products/details/<int:id>", views.product_details, name="product_details"),
    path("products/delete/<int:id>", views.product_delete, name="product_delete"),
    path("products/update/<int:id>", views.product_update, name="product_update"),
    path("products/add", views.product_add, name="product_add"),
    path("about", views.about, name="about"),
]
