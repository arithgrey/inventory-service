from celery import shared_task
from inventory.kafka_consumer import KafkaConsumer
import json

@shared_task
def consume_kafka_messages():
    print("llega")
    consumer = KafkaConsumer()
    try:
        consumer.consume_messages()
    except Exception as e:
        print(f"Error al consumir mensajes de Kafka: {e}")
    finally:
        consumer.close()