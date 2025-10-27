# Middleware-Rabbit
Middleware para conexión entre clientes y servidores de banco

## Configuración inicial de RabbitMQ

El script ```setup_rabbitmq.py``` despliega un contenedor usando la imagen de ```RabbitMQ``` con ```docker-compose```.

La configuración inicial del servidor de ```RabbitMQ``` incluye:

#### Bank Exchange
Es un **exchange directo** para las operaciones entre el cliente y el banco

Este exchange se enlaza a la cola **transaction queue** usando la *routing key* **transactions**

#### Verify Exchange
Es un **exchange directo** para las operaciones de verificación de identidad con Reniec

Este exchange se enlaza a la cola **verify queue** usando la *routing key* **verify**

## Instrucciones de uso

En Windows:
```
# Crea un entorno virtual
python -m venv venv
o
virtualenv venv

# Activa el entorno virtual
.\venv\Scripts\activate

# Instala las dependencias
pip install -r requirements.txt

# Ejecuta el script de despliegue del contenedor y configuración de RabbitMQ
python setup_rabbitmq.py start

# Para detener el contenedor ejecuta el siguiente comando
python setup_rabbitmq.py stop
```

En distribuciones Linux:
```
# Crea un entorno virtual
python3 -m venv venv

# Activa el entorno virtual
source venv/bin/activate

# Instala las dependencias
pip install -r requirements.txt

# Ejecuta el script de despliegue del contenedor y configuración inicial de RabbitMQ
python3 setup_rabbitmq.py start

# Para detener el contenedor ejecuta el siguiente comando
python3 setup_rabbitmq.py stop
```

Más documentación sobre el funcionamiento y los tipos de exchange de RabbitMQ [aquí](https://www.cloudamqp.com/blog/part4-rabbitmq-for-beginners-exchanges-routing-keys-bindings.html)