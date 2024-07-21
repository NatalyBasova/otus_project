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


def product_delete(request: HttpRequest, id: int) -> HttpResponse:
    product = Product.objects.get(id=id)

    if request.method == "POST":
        product.delete()
        return redirect("products")

    return render(
        request=request,
        template_name="product_delete.html",
        context={"product": product},
    )


def product_update(request: HttpRequest, id: int) -> HttpResponse:
    
    error = ""
    
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products")
        else:
            error = "Форма была неверной"

    product = Product.objects.get(id=id)
    form = ProductForm(instance=product)
    context = {"form": form, "error": error}

    return render(request=request, template_name="product_update.html", context=context)


def product_add(request: HttpRequest) -> HttpResponse:
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

    return render(request=request, template_name="product_add.html", context=context)


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")
