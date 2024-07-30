from .models import Product, Category
from django.forms import ModelForm, TextInput, Textarea, Select


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "quantity", "price", "category"]
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
            "category": Select(
                attrs={"class": "form-control", "placeholder": "Выберите категорию"}
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
