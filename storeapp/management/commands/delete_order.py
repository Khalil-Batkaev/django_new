from django.core.management.base import BaseCommand

from storeapp.models import Order


class Command(BaseCommand):
    help = 'Delete the order by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order id')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        order = Order.objects.filter(pk=pk).first()
        if order:
            order.delete()
        self.stdout.write(f'{order}')
