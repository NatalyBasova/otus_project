from django.db import migrations, models


# class Migration(migrations.Migration):

#     initial = True

#     dependencies = []

#     operations = [
#         migrations.CreateModel(
#             name="Product",
#             fields=[
#                 (
#                     "id",
#                     models.BigAutoField(
#                         auto_created=True,
#                         primary_key=True,
#                         serialize=False,
#                         verbose_name="ID",
#                     ),
#                 ),
#                 (
#                     "name",
#                     models.CharField(
#                         blank=True,
#                         max_length=100,
#                         null=True,
#                         verbose_name="Название товара",
#                     ),
#                 ),
#                 (
#                     "description",
#                     models.TextField(
#                         blank=True, null=True, verbose_name="Описание товара"
#                     ),
#                 ),
#                 (
#                     "quantity",
#                     models.IntegerField(
#                         blank=True, null=True, verbose_name="Количество товара"
#                     ),
#                 ),
#                 (
#                     "price",
#                     models.DecimalField(
#                         blank=True,
#                         decimal_places=2,
#                         max_digits=10,
#                         null=True,
#                         verbose_name="Цена товара",
#                     ),
#                 ),
#             ],
#             options={
#                 "verbose_name": "Товар",
#                 "verbose_name_plural": "Товары",
#             },
#         )
#     ]
