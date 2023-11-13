import argparse
import paho.mqtt.client as mqtt
import json

# Analizar los argumentos de la línea de comandos
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--developers', nargs='+', default=['all'], help='the developers the user is interested in')
parser.add_argument('-t', '--types', nargs='*', default=['all'], help='the types of videogames the user is interested in')
args = parser.parse_args()

# Crear un cliente MQTT
client = mqtt.Client()

# Definir la función de callback para cuando se reciba un mensaje
def on_message(client, userdata, message):
    videogame = json.loads(message.payload.decode())
    print(f'Recibimos: {videogame["name"]} with {videogame["discount"]}%')

client.on_message = on_message

# Conectar al broker MQTT
client.connect('localhost')

# Suscribirse a los temas correspondientes
for developer in args.developers:
    for type in args.types:
        topic = f'videogames/deals/{type}/{developer}'
        client.subscribe(topic)

# Comenzar el loop de red del cliente
client.loop_start()