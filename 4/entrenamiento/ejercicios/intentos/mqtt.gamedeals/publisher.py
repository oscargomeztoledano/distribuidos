#!/usr/bin/python3


import time
import paho.mqtt.client as mqtt
import json
from videogames import deals
# Crear un cliente MQTT
publisher = mqtt.Client()

# Conectar al broker MQTT
publisher.connect('127.0.0.1')


# Enviar un mensaje para cada videojuego en la lista
for videogame in deals:
    topic = f'videogames/deals/{videogame["type"]}/{videogame["developer"]}'
    message = json.dumps({'name': videogame['name'], 'discount': videogame['discount']})
    publisher.publish(topic, message)
    print(f'publicado  {videogame["name"]}')
    time.sleep(1)  # Esperar un segundo antes de enviar el siguiente mensaje


# Desconectar del broker MQTT
publisher.disconnect()