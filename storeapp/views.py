from django.shortcuts import render
from django.http import HttpResponse

STORE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <a href="/">Главная</a>
    <a href="#">Магазин</a>
    <h1>Магазин</h1>
    <a href="client/">Все клиенты</a><br>
    </p>
    <p>
    <a href="goods/">Все товары</a><br>
    </p>
    <p>
    <a href="order/">Все заказы</a><br>
    </p>
    <p>
  </body>
</html>
"""


def store(request):
    return HttpResponse(STORE)


def client(request):
    return HttpResponse('Clients')


def product(request):
    return HttpResponse('Goods')


def order(request):
    return HttpResponse('Orders')
