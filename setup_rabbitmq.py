import subprocess
import time
import pika
import sys

RABBIT_HOST = "localhost"
RABBIT_PORT = 5672
RABBIT_USER = "admin"
RABBIT_PASS = "admin"


def start_docker_compose():
    print("⚙️   Iniciando servicios con Docker Compose...")
    result = subprocess.run(["docker", "compose", "up", "-d"], capture_output=True, text=True)
    if result.returncode != 0:
        print("❌   Error al ejecutar docker compose:")
        print(result.stderr)
        sys.exit(1)
    print("✔   Docker Compose iniciado correctamente.\n")


def stop_container():
    print("🛑   Deteniendo servicios con Docker Compose...")
    result = subprocess.run(["docker", "compose", "down"], capture_output=True, text=True)
    if result.returncode != 0:
        print("❌   Error al detener los servicios:")
        print(result.stderr)
        sys.exit(1)
    print("✔   Servicios detenidos correctamente.\n")


def wait_for_rabbitmq(timeout=60):
    print("⏳  Esperando que RabbitMQ esté disponible...")
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            credentials = pika.PlainCredentials(RABBIT_USER, RABBIT_PASS)
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=RABBIT_HOST, port=RABBIT_PORT, credentials=credentials)
            )
            connection.close()
            print("✔   RabbitMQ está listo.\n")
            return True
        except pika.exceptions.AMQPConnectionError:
            time.sleep(3)
    print("❌   Timeout al esperar que RabbitMQ esté listo.")
    sys.exit(1)


def configure_rabbitmq():
    print("⚙️   Configurando RabbitMQ...")

    credentials = pika.PlainCredentials(RABBIT_USER, RABBIT_PASS)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBIT_HOST, port=RABBIT_PORT, credentials=credentials)
    )
    channel = connection.channel()

    # Exchange único para el middleware
    channel.exchange_declare(exchange='rabbit_exchange', exchange_type='direct', durable=True)

    channel.queue_declare(queue='bank_queue', durable=True)
    channel.queue_declare(queue='reniec_queue', durable=True)

    channel.queue_bind(exchange='rabbit_exchange', queue='bank_queue', routing_key='bank_operation')
    channel.queue_bind(exchange='rabbit_exchange', queue='reniec_queue', routing_key='reniec_operation')

    connection.close()
    print("✔   RabbitMQ configurado correctamente.\n")


def start_rabbit_server():
    start_docker_compose()
    wait_for_rabbitmq()
    configure_rabbitmq()
    print("✔   Middleware inicializado completamente.\n")


def main():
    if len(sys.argv) != 2:
        print("Comandos disponibles:")
        print("   - python script.py start   → Inicializa el sistema")
        print("   - python script.py stop    → Detiene el sistema")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "start":
        start_rabbit_server()
    elif command == "stop":
        stop_container()
    else:
        print(f"❌   Comando no reconocido: {command}")
        print("Usa 'start' o 'stop'")
        sys.exit(1)


if __name__ == "__main__":
    main()
