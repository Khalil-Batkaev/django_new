from django.core.management.base import BaseCommand

from storeapp.models import Client


class Command(BaseCommand):
    help = 'Delete the client by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client id')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        client = Client.objects.filter(pk=pk).first()
        if client:
            client.delete()
        self.stdout.write(f'{client}')
