import logging
from confluent_kafka import Consumer, KafkaError
from django.conf import settings
import json

logger = logging.getLogger(__name__)

class KafkaConsumer:
    def __init__(self):
        self.bootstrap_servers = settings.KAFKA_BOOTSTRAP_SERVERS
        self.consumer = Consumer({
            'bootstrap.servers': self.bootstrap_servers,
            'group.id': 'order_consumer_group',
            'auto.offset.reset': 'earliest'
        })
        self.consumer.subscribe([settings.KAFKA_ORDER_TOPIC])

    def consume_messages(self):        
        try:
            while True:
                msg = self.consumer.poll(1.0)

                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        continue
                    else:
                        #print(f"Error al consumir mensaje: {msg.error()}")
                        logger.error(f"Error al consumir mensaje: {msg.error()}")

                        break

                order_data = json.loads(msg.value().decode('utf-8'))
                #print(f"Mensaje recibido: {order_data}")
                logger.info(f"Mensaje recibido: {order_data}")


        except KeyboardInterrupt:
            pass
        finally:
            self.close()
            
    def close(self):
        self.consumer.close()