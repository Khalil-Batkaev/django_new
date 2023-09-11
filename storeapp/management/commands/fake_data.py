import random
from datetime import datetime,timedelta

from django.core.management.base import BaseCommand

from storeapp.models import Product, Client, Order


class Command(BaseCommand):
    QTY = 30
    CLIENT_ID = 4
    help = 'Add fake data'

    def handle(self, *args, **kwargs):
        for i in range(1, self.QTY + 1):
            product = Product(
                name=f'Product_{i}',
                description=f'Product_{i} is very nice',
                price=1999.99,
                qty=10
            )
            product.save()

        client = Client.objects.filter(pk=self.CLIENT_ID).first()

        for i in range(1, self.QTY):
            order = Order(
                client=client,
                total_amount=random.randint(1000, 10_000),
                created_at=datetime.now() - timedelta(random.randint(1, 365))
            )
            order.save()
            for _ in range(5):
                product = Product.objects.filter(pk=random.randint(1, 30)).first()
                order.product.add(product)

        self.stdout.write(f'all done')
