import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, UpdateView

from storeapp import forms
from storeapp.models import Client, Product, Order


def store(request):
    return render(request, 'storeapp/store.html', {'title': 'Наш магазин', 'client_id': 4, 'product_id': 2})


def client(request):
    clients = Client.objects.all()
    return render(request, 'storeapp/clients.html', {'title': 'Все клиенты', 'clients': clients})


def product(request):
    goods = Product.objects.all()
    return render(request, 'storeapp/goods.html', {'title': 'Все продукты', 'goods': goods})


def order(request):
    orders = Order.objects.all()
    return render(request, 'storeapp/orders.html', {'title': 'Все заказы', 'orders': orders})


def orders_of_client(request, client_id, period=None):
    DAYS = {
        'week': 7,
        'month': 31,
        'year': 365
    }
    if period:
        pivot = datetime.datetime.now() - datetime.timedelta(DAYS.get(period))
        orders = Order.objects.filter(client_id=client_id) & Order.objects.filter(created_at__gt=pivot)
    else:
        orders = Order.objects.filter(client_id=client_id)
    return render(request, 'storeapp/client_orders.html', {'title': 'Заказы клиента', 'orders': orders,
                                                           'period': period})


def goods_of_client(request, order_id):
    goods = Order.objects.filter(pk=order_id).first().product.all()
    return render(request, 'storeapp/order_detail.html', {'title': 'Товары клиента', 'goods': goods})


class ProductDetail(DetailView):
    model = Product
    template_name = 'storeapp/product_detail.html'


class UpdateProduct(UpdateView):
    model = Product
    template_name = 'storeapp/update_product.html'
    form_class = forms.UpdateProductForm

