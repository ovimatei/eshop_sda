from django.urls import path

from cart import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('edit/<int:id>/', views.cart_item_edit, name='edit'),
    path('delete/<int:id>/', views.cart_item_delete, name='delete'),
    path('list/', views.cart_list, name='list'),
    path('add/', views.cart_item_add, name='add'),
]