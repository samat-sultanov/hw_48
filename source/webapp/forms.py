from django import forms
from django.forms import widgets

from webapp.models import CATEGORY_CHOICES


class SearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Наименование товара")


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Наименование товара")
    description = forms.CharField(max_length=2000, required=False, label="Описание товара",
                                  widget=widgets.Textarea(attrs={'cols': 40, 'rows': 3}))
    category = forms.ChoiceField(widget=forms.Select(), choices=CATEGORY_CHOICES, initial=CATEGORY_CHOICES[0][0],
                                 required=True, label="Категория товара")
    balance = forms.IntegerField(min_value=0, required=True, label="Остаток")
    price = forms.DecimalField(max_digits=7, decimal_places=2, required=True, label="Цена")
