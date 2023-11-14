#!/usr/bin/python3

import paho.mqtt.client as mqtt
import json
import time

codeTopic=f'ssdd/ejercicio04/person/code'
resultTopic=f'ssdd/ejercicio04/person/results'


def on_connect(client, userdata, flags, rc):
    subscriber.subscribe(codeTopic)

def on_message(client, userdata, msg):
    code = msg.payload.decode()
    print(f'Code: {code}')
    data={
        'code':code,
        'fullname':'Oscar Gomez Toledano',
        'dni':'04864501'
    }
    subscriber.publish(resultTopic
                      ,json.dumps(data))
    time.sleep(1)

subscriber = mqtt.Client()
subscriber.on_connect = on_connect
subscriber.on_message = on_message
subscriber.connect('192.168.8.224')

print('Waiting for code...')
try:
    subscriber.loop_forever()
except KeyboardInterrupt:
    print('EXIT')
    subscriber.disconnect()
