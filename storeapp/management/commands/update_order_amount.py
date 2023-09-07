import decimal

from django.core.management.base import BaseCommand

from storeapp.models import Order


class Command(BaseCommand):
    help = 'Update total amount of the order'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order id')
        parser.add_argument('total_amount', type=decimal.Decimal, help='Total amount')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        total_amount = kwargs.get('total_amount')
        order = Order.objects.filter(pk=pk).first()
        if order:
            order.total_amount = total_amount
            order.save()
        self.stdout.write(f'{order}')
