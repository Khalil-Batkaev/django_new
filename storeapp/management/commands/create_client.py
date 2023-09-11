from django.core.management.base import BaseCommand

from storeapp.models import Client


class Command(BaseCommand):
    help = 'Add new client'

    def handle(self, *args, **kwargs):
        client = Client(
            name='Ivan',
            email='test@test.ru',
            phone=9284563215,
            address='Kazan, Podedy str, 12-48',
        )
        client.save()
        self.stdout.write(f'{client}')
