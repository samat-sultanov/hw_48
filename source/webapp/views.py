from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import Product
from webapp.forms import SearchForm


def index_view(request):
    form = SearchForm(data=request.GET)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        context = {
            'products': Product.objects.filter(name__iexact=name).filter(balance__gt=0).order_by('category', 'name')
        }
        return render(request, 'index_view.html', context)
    else:
        products = Product.objects.filter(balance__gt=0).order_by('category', 'name')
        context = {
            'products': products
        }
    return render(request, 'index_view.html', context)


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'product_view.html', context)
