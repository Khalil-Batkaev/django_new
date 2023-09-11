from django.core.management.base import BaseCommand

from storeapp.models import Order, Client, Product


class Command(BaseCommand):
    help = 'Add new order'

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int, help="Client's id")
        parser.add_argument('goods_id', type=tuple, help="Goods id")

    def handle(self, *args, **kwargs):
        client_id = kwargs.get('client_id')
        goods_id = map(int, kwargs.get('goods_id'))
        client = Client.objects.filter(pk=client_id).first()
        order = Order(
            client=client,
            total_amount=5000.00
        )
        order.save()
        for product_id in goods_id:
            product = Product.objects.filter(pk=product_id).first()
            order.product.add(product)

        self.stdout.write(f'{order}')
