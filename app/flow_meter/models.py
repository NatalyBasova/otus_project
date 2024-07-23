from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Название товара", null=True, blank=True
    )
    description = models.TextField(
        verbose_name="Описание товара", null=True, blank=True
    )
    quantity = models.IntegerField(
        verbose_name="Количество товара", null=True, blank=True
    )
    price = models.DecimalField(
        max_digits=10,
        verbose_name="Цена товара",
        decimal_places=2,
        null=True,
        blank=True,
    )
    category = models.TextField(max_length=12, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
