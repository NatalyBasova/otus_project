from django.contrib import admin
from django.urls import path, include


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("products/", views.all_products, name="products"),
    # path("add_product", views.add_product, name="add_product"),
    path("about", views.about, name="about"),
]
