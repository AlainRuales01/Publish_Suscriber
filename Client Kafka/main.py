from kafka import KafkaConsumer


# Configura la dirección del servidor Kafka y el nombre del topic
bootstrap_servers = 'localhost:9092'
topic_name = 'test'

# Crea un consumidor Kafka
consumer = KafkaConsumer(topic_name, bootstrap_servers=bootstrap_servers)

# Comienza a consumir mensajes del topic
for message in consumer:
    # El mensaje es un objeto de tipo ConsumerRecord
    # Puedes acceder al contenido del mensaje utilizando el atributo 'value'
    print("Received message: {}".format(message.value.decode('utf-8')))
