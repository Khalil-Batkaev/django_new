from django.core.management.base import BaseCommand

from storeapp.models import Product


class Command(BaseCommand):
    help = 'Read all goods'

    def handle(self, *args, **kwargs):
        goods = Product.objects.all()
        self.stdout.write(f'{goods}')
