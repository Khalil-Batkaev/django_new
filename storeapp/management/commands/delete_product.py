from django.core.management.base import BaseCommand

from storeapp.models import Product


class Command(BaseCommand):
    help = 'Delete the product by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help="Product's id")

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        if product:
            product.delete()
        self.stdout.write(f'{product}')
