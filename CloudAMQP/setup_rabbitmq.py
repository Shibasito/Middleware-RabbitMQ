import pika

# URL de conexión completa de CloudAMQP
# URL de servidor RabbitMQ configurado: "amqps://jpzcqbdk:d-3-hU6-01rwT7cfKH7OJGE0f67-Av-G@fly.rmq.cloudamqp.com/jpzcqbdk"
CLOUDAMQP_URL = "TU URL DE CONEXIÓN CLOUDAMQP"

# Establecer conexión segura
params = pika.URLParameters(CLOUDAMQP_URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()

print("⚙️   Configurando RabbitMQ...")

# Exchange y cola para transacciones bancarias
channel.exchange_declare(exchange='bank_exchange', exchange_type='direct', durable=True)
channel.queue_declare(queue='transactions_queue', durable=True)
channel.queue_bind(exchange='bank_exchange', queue='transactions_queue', routing_key='transactions')

# Exchange y cola para verificación de identidad
channel.exchange_declare(exchange='verify_exchange', exchange_type='direct', durable=True)
channel.queue_declare(queue='verify_queue', durable=True)
channel.queue_bind(exchange='verify_exchange', queue='verify_queue', routing_key='verify')

connection.close()
print("✔   RabbitMQ configurado correctamente.\n")

