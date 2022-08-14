import email
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        u = User(username='samar',
                email='samararora99@gmail.com',
                password='samar')
        u.save()
        u2 = User(username='samar2',
                email = 'scipioresearch2020@gmail.com',
                password='samar')
        u2.save()

        self.stdout.write('Successfully added user to the database')