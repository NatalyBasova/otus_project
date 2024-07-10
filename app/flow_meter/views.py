from django.shortcuts import render, redirect
from django.template import loader

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
# from .models import Product
# from .forms import ProductForm


def index(request) -> HttpResponse:
    # products = Product.objects.order_by("-id")
    # context = {"title": "Главная страница сайта", "products": products}
    # return render(request, "templates/index.html", context)
    # template = loader.get_template( "templates/index.html")
    # return HttpResponse(template.render())
    return render(request, "templates/index.html")
    


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


# def about(request):
#     return render(request, "tempates/about.html")
