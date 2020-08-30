from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def list_products(request):
    return render(request, 'products.html')


def home_page(request):
    context = {
        "title": "Home",
    }

    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')
