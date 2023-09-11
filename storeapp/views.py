from django.shortcuts import render
from django.http import HttpResponse

from storeapp.models import Client, Product, Order


def store(request):
    return render(request, 'storeapp/store.html', {'title': 'Наш магазин'})


def client(request):
    clients = Client.objects.all()
    return render(request, 'storeapp/clients.html', {'title': 'Все клиенты', 'clients': clients})


def product(request):
    goods = Product.objects.all()
    return render(request, 'storeapp/goods.html', {'title': 'Все продукты', 'goods': goods})


def order(request):
    orders = Order.objects.all()
    return render(request, 'storeapp/orders.html', {'title': 'Все заказы', 'orders': orders})
