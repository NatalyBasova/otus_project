from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, Http404
from django.core.paginator import InvalidPage, Paginator
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
)
from django.urls import reverse_lazy, reverse

from .models import Product, Category
from .forms import ProductForm, CategoryForm


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


class ProductListView(ListView):
    model = Product
    paginate_by = 10


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("products")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("products")
    template_name = "flow_meter/product_update.html"


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("products")


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")


class CategoryListView(ListView):
    model = Category
    paginate_by = 10


class CategoryDetailView(DetailView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("categories")


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("categories")
    template_name = "flow_meter/category_update.html"


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy("categories")
