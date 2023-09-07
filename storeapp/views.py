from django.shortcuts import render
from django.http import HttpResponse


def client(request):
    return HttpResponse('Clients')


def product(request):
    return HttpResponse('Goods')


def order(request):
    return HttpResponse('Orders')
