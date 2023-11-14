import json
import paho.mqtt.client as mqtt


def callback(client, userdata, message):
    code= message.payload.decode()
    print(code)
    data={
        'code':code,
        'fullname':'Oscar Gomez Toledano',
        'dni':'04864501'
    }
    cliente.publish('ssdd/ejercicio04/person/results',json.dumps(data))
    print('mensaje enviado')
    cliente.disconnect()



cliente = mqtt.Client()
cliente.on_message = callback
cliente.connect('192.168.8.224')
cliente.subscribe('ssdd/ejercicio04/person/codes')




try:
    cliente.loop_forever()
except KeyboardInterrupt:
    pass