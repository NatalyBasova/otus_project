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
    path("categories/", views.all_categories, name="categories"),
    # path("category/details/<int:id>", views.category_details, name="category_details"),
    # path("category/delete/<int:id>", views.category_delete, name="category_delete"),
    # path("category/update/<int:id>", views.category_update, name="category_update"),
    path("categories/add", views.category_add, name="category_add"),
]
