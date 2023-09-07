from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('goods/', views.product, name='goods'),
    path('order/', views.order, name='order'),
    path('client/', views.client, name='client'),
]
