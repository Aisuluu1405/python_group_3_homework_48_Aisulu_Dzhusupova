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


def product_edit_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(data={
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'count': product.count,
            'price':product.price
        })
        return render(request, 'product_edit.html', context={'form': form, 'product': product})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            product.name = data['name']
            product.description = data['description']
            product.category = data['category']
            product.count = data['count']
            product.price = data['price']
            product.save()
            return redirect('product_path', pk=product.pk)
        else:
            return render(request, 'product_edit.html', context={'form': form, 'product': product})


def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'product_delete.html', context={'product': product})
    elif request.method == 'POST':
        product.delete()
    return redirect('index')
