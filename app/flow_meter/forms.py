from .models import Product, Category
from django.forms import ModelForm, TextInput, Textarea


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "quantity", "price"]
        widgets = {
            "name": TextInput(
                attrs={"class": "form-control", "placeholder": "Введите товар"}
            ),
            "description": Textarea(
                attrs={"class": "form-control", "placeholder": "Введите описание"}
            ),
            "quantity": TextInput(
                attrs={"class": "form-control", "placeholder": "Введите кол-во товара"}
            ),
            "price": TextInput(
                attrs={"class": "form-control", "placeholder": "Введите цену товара"}
            ),
        }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        widgets = {
            "name": TextInput(
                attrs={"class": "form-control", "placeholder": "Введите категорию"}
            ),
        }
