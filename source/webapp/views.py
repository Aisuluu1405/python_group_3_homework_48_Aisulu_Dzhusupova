from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import ProductForm
from webapp.models import Product


def index_view(request, *args, **kwargs):
    products = Product.objects.filter(count__gt=0).order_by('category', 'name')
    return render(request, 'index.html', context={
        'products': products
    })


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_view.html', context={
        'product': product
    })


def product_add_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'product_add.html', context={'form': form})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            product = Product.objects.create(
                name=data['name'],
                description=data['description'],
                category=data['category'],
                count=data['count'],
                price=data['price']
            )
            return redirect('index')
        else:
            return render(request, 'product_add.html', context={'form': form})


