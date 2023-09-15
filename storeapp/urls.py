from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('goods/', views.product, name='goods'),
    path('order/', views.order, name='order'),
    path('client/', views.client, name='client'),
    path('order/client/<int:client_id>/', views.orders_of_client, name='client_orders'),
    path('goods/order/<int:order_id>/', views.goods_of_client, name='client_goods'),
    path('order/client/<int:client_id>/<str:period>/', views.orders_of_client, name='client_orders_period'),
    path('goods/product/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('goods/product/create/', views.CreateProduct.as_view(), name='create_product'),
    path('goods/product/<int:pk>/update/', views.UpdateProduct.as_view(), name='update_product'),
]
