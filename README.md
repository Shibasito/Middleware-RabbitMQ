# Middleware-Rabbit
Middleware para conexión entre clientes y servidores de banco

## Configuración inicial de RabbitMQ

El script ```setup_rabbitmq.py``` despliega un contenedor usando la imagen de ```RabbitMQ``` con ```docker-compose```.

La configuración inicial del servidor de ```RabbitMQ``` incluye:

#### Rabbit Exchange
Es un **exchange directo** para las operaciones entre el cliente, el banco y RENIEC 

Este exchange se enlaza a la cola **bank_queue** usando la *routing key* **bank_operation**
Este exchange se enlaza a la cola **reniec_queue** usando la *routing key* **reniec_operation**

#### Configuración de credenciales de usuario
```
RABBIT_HOST = "localhost"
RABBIT_PORT = 5672
RABBIT_USER = "admin"
RABBIT_PASS = "admin"
```


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

## Despliegue de RabbitMQ con CloudAMQP

Para desplegar un servidor de **RabbitMQ** en la nube, puedes acceder a [CloudMQ](https://www.cloudamqp.com/), crearte una cuenta y crear una instancia de **RabbitMQ** fácilmente.

Una vez creada tu instancia, puedes configurar el servidor ingresando al **RabbitMQ Manager** o mediante código usando la URL de conexión que aparece en el apartado **AMQP details**, la cual tiene tiene el formato ```amqps://user:password@fly.rmq.cloudamqp.com/user```

Para realizar la misma configuración de **exchanges** y **colas** de este repositorio, puedes ejecutar el script ```CloudAMQP/setup_rabbitmq.py``` luego de activar el entorno virtual e instalar las dependencias como se indica el las *instrucciones de uso*.


Más documentación sobre el funcionamiento y los tipos de exchange de RabbitMQ [aquí](https://www.cloudamqp.com/blog/part4-rabbitmq-for-beginners-exchanges-routing-keys-bindings.html)