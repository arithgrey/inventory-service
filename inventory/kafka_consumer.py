from kafka import KafkaConsumer

def kafka_consumer():
    consumer = KafkaConsumer('new_order', bootstrap_servers=['localhost:9092'])
    for message in consumer:
        
        print("Mensaje recibido:", message.value)
        

if __name__ == "__main__":
    kafka_consumer()