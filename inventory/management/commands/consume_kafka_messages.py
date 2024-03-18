from django.core.management.base import BaseCommand
from inventory.tasks import consume_kafka_messages  

class Command(BaseCommand):
    help = 'Inicia la tarea de Celery para consumir mensajes de Kafka'

    def handle(self, *args, **options):
        consume_kafka_messages.delay()
        self.stdout.write(self.style.SUCCESS('Tarea de Celery para consumir mensajes de Kafka iniciada correctamente.'))