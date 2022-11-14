from django import forms
from django.forms import widgets


class SearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Наименование товара")