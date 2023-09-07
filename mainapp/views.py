import logging

from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)

INDEX = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <a href="#">Главная</a>
    <a href="about/">О нас</a>
    <h1>Главная страница</h1>
    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugit odit in rerum aperiam illum, soluta sit repellat
      accusamus officia ea unde? Aliquid dicta soluta vel accusamus impedit, fuga officiis perspiciatis?
    </p>
    <h2>Добро пожаловать на сайт</h2>
    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Hic laudantium deserunt ea natus. Excepturi commodi
      ipsum, deserunt soluta odit facere deleniti sint? Ad exercitationem, inventore maxime aliquid minima dolore culpa
      quas amet repellat perspiciatis unde odio officia quo, distinctio numquam minus doloremque fugiat libero, harum
      tempore ullam? Hic, ab libero.
    </p>
    <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Reprehenderit, enim.</p>
    <p>
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dignissimos, reprehenderit minima. Consectetur sed
      neque, unde aperiam perferendis voluptatum, odit, atque repudiandae maxime architecto ut distinctio!
    </p>
  </body>
</html>
"""

ABOUT = """
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
    <a href="#">О нас</a>
    <h1>О нас</h1>
    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugit odit in rerum aperiam illum, soluta sit repellat
      accusamus officia ea unde? Aliquid dicta soluta vel accusamus impedit, fuga officiis perspiciatis?
    </p>
    <h2>О нашем проекте</h2>
    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Hic laudantium deserunt ea natus. Excepturi commodi
      ipsum, deserunt soluta odit facere deleniti sint? Ad exercitationem, inventore maxime aliquid minima dolore culpa
      quas amet repellat perspiciatis unde odio officia quo, distinctio numquam minus doloremque fugiat libero, harum
      tempore ullam? Hic, ab libero.
    </p>
    <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Reprehenderit, enim.</p>
    <p>
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dignissimos, reprehenderit minima. Consectetur sed
      neque, unde aperiam perferendis voluptatum, odit, atque repudiandae maxime architecto ut distinctio!
    </p>
  </body>
</html>
"""


def index(request):
    logger.info('Index page accessed')
    return HttpResponse(INDEX)


def about(request):
    logger.info('About us page accessed')
    return HttpResponse(ABOUT)
