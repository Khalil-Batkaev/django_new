from django.core.management.base import BaseCommand

from storeapp.models import Order


class Command(BaseCommand):
    help = 'Read all orders'

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()

        self.stdout.write(f'{orders}')
