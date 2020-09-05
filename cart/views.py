from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def cart(request):
    return HttpResponse("Hello cart")


def cart_item_edit(request, id):
    return HttpResponse('')


def cart_item_delete(request, id):
    return HttpResponse('')


def cart_list(request):
    return HttpResponse('')


def cart_item_add(request):
    return HttpResponse('')
