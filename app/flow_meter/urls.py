from django.contrib import admin
from django.urls import path, include


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("products/", views.ProductListView.as_view(), name="products"),
    path("products/details/<int:pk>", views.ProductDetailView.as_view(), name="product_details"),
    path("products/delete/<int:pk>", views.ProductDeleteView.as_view(), name="product_delete"),
    path("products/update/<int:pk>", views.ProductUpdateView.as_view(), name="product_update"),
    path("products/add", views.ProductCreateView.as_view(), name="product_create"),
    path("about", views.about, name="about"),
    # path("categories/", views.all_categories, name="categories"),
    # path("categories/details/<int:id>", views.category_details, name="category_details"),
    # path("categories/delete/<int:id>", views.category_delete, name="category_delete"),
    # path("categories/update/<int:id>", views.category_update, name="category_update"),
    # path("categories/add", views.category_add, name="category_add"),
]
