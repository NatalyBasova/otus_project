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

from django.contrib.auth.mixins import PermissionRequiredMixin

# from django.contrib.auth.decorators import login_required, permission_required


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


class ProductListView(PermissionRequiredMixin, ListView):
    model = Product
    paginate_by = 10
    permission_required = "flow_meter.view_product"


class ProductDetailView(PermissionRequiredMixin, DetailView):
    model = Product
    permission_required = "flow_meter.view_product"


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("products")
    permission_required = "flow_meter.add_product"


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("products")
    template_name = "flow_meter/product_update.html"
    permission_required = "flow_meter.change_product"


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("products")
    permission_required = "flow_meter.delete_product"


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")


class CategoryListView(PermissionRequiredMixin, ListView):
    model = Category
    paginate_by = 10
    permission_required = "flow_meter.view_category"


class CategoryDetailView(PermissionRequiredMixin, DetailView):
    model = Category
    permission_required = "flow_meter.view_category"


class CategoryCreateView(PermissionRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("categories")
    permission_required = "flow_meter.add_category"


class CategoryUpdateView(PermissionRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("categories")
    template_name = "flow_meter/category_update.html"
    permission_required = "flow_meter.change_category"


class CategoryDeleteView(PermissionRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy("categories")
    permission_required = "flow_meter.delete_category"
