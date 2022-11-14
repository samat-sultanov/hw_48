from django.db import models

CATEGORY_CHOICES = [('other', 'разное'), ('food', 'еда'), ('drinks', 'напитки')]


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Наименование товара")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Описание товара")
    category = models.CharField(max_length=30, null=False, blank=False, choices=CATEGORY_CHOICES,
                                default=CATEGORY_CHOICES[0][0])
    balance = models.PositiveIntegerField(verbose_name="Остаток")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время редактирования")

    def __str__(self):
        return f"Товар {self.id}: {self.name}"
