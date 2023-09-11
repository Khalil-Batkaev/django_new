import decimal

from django.core.management.base import BaseCommand

from storeapp.models import Product


class Command(BaseCommand):
    help = 'Update the price of product by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help="Product's id")
        parser.add_argument('price', type=decimal.Decimal, help="Price of the product")

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        price = kwargs.get('price')
        product = Product.objects.filter(pk=pk).first()
        if product:
            product.price = price
            product.save()
        self.stdout.write(f'{product}')
