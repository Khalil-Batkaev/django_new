from django.core.management.base import BaseCommand

from storeapp.models import Client


class Command(BaseCommand):
    help = 'Read all client'

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        self.stdout.write(f'{clients}')
