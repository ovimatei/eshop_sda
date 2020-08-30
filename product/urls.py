from django.urls import path

from product.views import list_products, home_page, about

urlpatterns =[
    path('products/', list_products, name="list_products"),
    path('', home_page, name='home'),
    path('about/', about, name='about')
]