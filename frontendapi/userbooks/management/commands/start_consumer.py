from django.core.management.base import BaseCommand
from ...consumer import start_consuming

class Command(BaseCommand):
    help = 'Start RabbitMQ consumer to sync book data'

    def handle(self, *args, **kwargs):
        start_consuming()
