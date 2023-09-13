import logging

from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return render(request, 'mainapp/index.html', {'title': 'Главная страница'})


def about(request):
    logger.info('About us page accessed')
    return render(request, 'mainapp/about.html', {'title': 'О нас'})
