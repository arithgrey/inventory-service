from rest_framework import viewsets, status
from rest_framework.response import Response
from inventory.kafka_consumer import KafkaConsumer

class InventoryView(viewsets.ViewSet):
    
    def list(self, request):
        
        consumer = KafkaConsumer()
                
        messages = consumer.consume_messages()
        
        consumer.close()
                
        return Response(messages, status=status.HTTP_200_OK)