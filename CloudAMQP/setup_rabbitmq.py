import pika

# URL de conexión completa de CloudAMQP
# URL de servidor RabbitMQ configurado: "amqps://jpzcqbdk:d-3-hU6-01rwT7cfKH7OJGE0f67-Av-G@fly.rmq.cloudamqp.com/jpzcqbdk"
CLOUDAMQP_URL = "TU URL DE CONEXIÓN CLOUDAMQP"

# Establecer conexión segura
params = pika.URLParameters(CLOUDAMQP_URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()

print("⚙️   Configurando RabbitMQ...")

channel.exchange_declare(exchange='rabbit_exchange', exchange_type='direct', durable=True)

channel.queue_declare(queue='bank_queue', durable=True)
channel.queue_declare(queue='reniec_queue', durable=True)

channel.queue_bind(exchange='rabbit_exchange', queue='bank_queue', routing_key='bank_operation')
channel.queue_bind(exchange='rabbit_exchange', queue='reniec_queue', routing_key='reniec_operation')


connection.close()
print("✔   RabbitMQ configurado correctamente.\n")

