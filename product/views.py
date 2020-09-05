from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import resolve

from product.models import Product, ProductImage


def list_products(request):
    placeholder_picture = 'https://thumbs.dreamstime.com/b/no-thumbnail-image-placeholder-forums-blogs-websites-148010362.jpg'
    current_url = resolve(request.path_info).url_name
    all_products = Product.objects.all()
    all_product_images = []
    for product in all_products:
        product_images = ProductImage.objects.filter(selected_product=product.id)
        if len(product_images) > 0:
            first_image_url = product_images[0].url
            all_product_images.append(first_image_url)
        else:
            all_product_images.append(placeholder_picture)

    context = {
        "products": all_products,
        "current_url": current_url,
        'images': all_product_images,
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
        product_images = ProductImage.objects.filter(selected_product=id_)
        if len(product_images) > 0:
            context['images'] = product_images

    else:
        return HttpResponse('Product not found')

    return render(request, 'product_details.html', context)
