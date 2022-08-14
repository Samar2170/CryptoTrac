from django.core.management.base import BaseCommand
from core.models import Coin

class Command(BaseCommand):
    def handle(self, *args, **options):
        c = Coin(name='Bitcoin', symbol='BTC', coingecko_id='bitcoin')
        c.save()
        self.stdout.write('Successfully added Bitcoin coin to the database')
        