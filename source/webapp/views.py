from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import Product
from webapp.forms import SearchForm, ProductForm


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


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        return render(request, "delete_product.html", {"product": product})
    elif request.method == "POST":
        product.delete()
        return redirect("index_view")


def create_product(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, "create_product.html", {'form': form})
    elif request.method == "POST":
        form = ProductForm(data=request.POST)
        if form.is_valid():
            Product.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                balance=form.cleaned_data['balance'],
                price=form.cleaned_data['price']
            )
            return redirect('index_view')
        else:
            return render(request, 'create_product.html', {'form': form})


def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        form = ProductForm(initial={
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'balance': product.balance,
            'price': product.price
        })
        return render(request, 'update_product.html', {'form': form})
    elif request.method == "POST":
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data.get('name')
            product.description = form.cleaned_data.get('description')
            product.category = form.cleaned_data.get('category')
            product.balance = form.cleaned_data.get('balance')
            product.price = form.cleaned_data.get('price')
            product.save()
            return redirect('index_view')
        else:
            return render(request, 'update_product.html', {'form': form})
