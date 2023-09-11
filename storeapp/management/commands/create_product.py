from django.core.management.base import BaseCommand

from storeapp.models import Product


class Command(BaseCommand):
    help = 'Add new product'

    def handle(self, *args, **kwargs):
        product = Product(
            name='Iphone',
            description='Phone',
            price=1999.99,
            qty=10
        )
        product.save()
        self.stdout.write(f'{product}')
