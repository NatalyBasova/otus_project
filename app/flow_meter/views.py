from django.shortcuts import render, redirect


# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from .models import Product

# from .forms import ProductForm


def index(request: HttpRequest) -> HttpResponse:
    # products = Product.objects.order_by("-id")
    # context = {"title": "Главная страница сайта", "products": products}
    # return render(request, "templates/index.html", context)
    # template = loader.get_template( "templates/index.html")
    # return HttpResponse(template.render())
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


# def add_product(request):
#     error = ""
#     if request.method == "POST":
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("index")
#         else:
#             error = "Форма была не верной"
#         form = ProductForm()
#         context = {"form": form, "error": error}

#         return render(request, "templates/add_product.html", context)


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")
