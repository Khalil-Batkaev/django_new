from django.shortcuts import render
from django.http import HttpResponse

from storeapp.models import Client, Product, Order


def store(request):
    return render(request, 'storeapp/store.html', {'title': 'Наш магазин'})


def client(request):
    clients = Client.objects.all()
    return HttpResponse(clients)


def product(request):
    goods = Product.objects.all()
    return HttpResponse(goods)


def order(request):
    orders = Order.objects.all()
    return HttpResponse(orders)
