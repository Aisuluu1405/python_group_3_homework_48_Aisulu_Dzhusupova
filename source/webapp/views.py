from django.shortcuts import render, get_object_or_404, redirect
# from webapp.forms import ProductForm
from webapp.models import Product


def index_view(request, *args, **kwargs):
    products = Product.objects.all()
    return render(request, 'index.html', context={
        'products': products
    })

