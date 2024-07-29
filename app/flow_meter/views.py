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


# def all_categories(request: HttpRequest) -> HttpResponse:
#     categories = Category.objects.all().values()

#     return render(
#         request=request,
#         template_name="all_categories.html",
#         context={"categories": categories},
#     )


# def category_details(request: HttpRequest, id: int) -> HttpResponse:
#     category = Category.objects.get(id=id)

#     return render(
#         request=request,
#         template_name="category_details.html",
#         context={"category": category},
#     )


# def category_delete(request: HttpRequest, id: int) -> HttpResponse:
#     category = Category.objects.get(id=id)

#     if request.method == "POST":
#         category.delete()
#         return redirect("categories")

#     return render(
#         request=request,
#         template_name="category_delete.html",
#         context={"category": category},
#     )


# def category_update(request: HttpRequest, id: int) -> HttpResponse:

#     category = Category.objects.get(id=id)
#     error = ""

#     if request.method == "POST":
#         form = CategoryForm(request.POST, instance=category)
#         if form.is_valid():
#             form.save()
#             return redirect("categories")
#         else:
#             error = "Форма была неверной"
#     else:
#         form = CategoryForm(instance=category)

#     context = {"form": form, "error": error}

#     return render(
#         request=request, template_name="category_update.html", context=context
#     )


# def category_add(request: HttpRequest) -> HttpResponse:
#     error = ""
#     if request.method == "POST":
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("categories")
#         else:
#             error = "Форма была неверной"

#     form = CategoryForm()
#     context = {"form": form, "error": error}

#     return render(request=request, template_name="category_add.html", context=context)
