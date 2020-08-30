from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import resolve

from product.models import Product


def list_products(request):
    current_url = resolve(request.path_info).url_name
    all_products = Product.objects.all()
    context = {
        "products": all_products,
        "current_url": current_url,
    }
    return render(request, 'products.html', context)


def home_page(request):
    context = {
        "title": "Home",
    }

    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def product_details(request, id_):
    context = {}

    products = Product.objects.filter(id=id_)
    if len(products) > 0:
        context['name'] = products[0].name
        context['description'] = products[0].description
        context['price'] = products[0].price
        context['picture'] = products[0].picture
    else:
        return HttpResponse('Product not found')

    return render(request, 'product_details.html', context)
