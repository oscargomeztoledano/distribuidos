import time
import paho.mqtt.client as mqtt
import json
import videogames  # Importar el módulo videogames

# Crear un cliente MQTT
client = mqtt.Client()

# Conectar al broker MQTT
client.connect('localhost')

# Obtener la lista de videojuegos del módulo videogames
videogames_list = videogames.deals

# Enviar un mensaje para cada videojuego en la lista
for videogame in videogames_list:
    topic = f'videogames/deals/{videogame["type"]}/{videogame["developer"]}'
    message = json.dumps({'name': videogame['name'], 'discount': videogame['discount']})
    client.publish(topic, message)
    print(f'publicado  {videogame["name"]}')
    time.sleep(1)  # Esperar un segundo antes de enviar el siguiente mensaje