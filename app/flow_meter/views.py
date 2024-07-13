from django.shortcuts import render, redirect


# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest

from .models import Product
from .forms import ProductForm


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


def all_products(request: HttpRequest) -> HttpResponse:
    products = Product.objects.all().values()

    return render(
        request=request,
        template_name="all_products.html",
        context={"products": products},
    )


def product_details(request: HttpRequest, id: int) -> HttpResponse:
    product = Product.objects.get(id=id)

    return render(
        request=request,
        template_name="product_details.html",
        context={"product": product},
    )


def add_product(request: HttpRequest) -> HttpResponse:
    error = ""
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products")
        else:
            error = "Форма была неверной"
        form = ProductForm()
        context = {"form": form, "error": error}

    return render(request=request, template_name="add_product.html", context=context)


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")
