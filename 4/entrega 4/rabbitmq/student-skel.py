#!/usr/bin/python3

import pika
import json

class App:
    def __init__(self, broker_host):
        self.broker_host = broker_host
        self.parameters = pika.ConnectionParameters(host=self.broker_host)
        self.code_connection = pika.BlockingConnection(self.parameters)
        self.code_channel = self.code_connection.channel()
        self.code_channel.queue_declare(queue='codes')
        self.code_channel.basic_consume(
            queue='codes',
            auto_ack=True,
            on_message_callback=self.callback
        )
        self.code_channel.start_consuming()

    def callback(self, ch, method, props, body):
        self.code_connection.close()
        code= body.decode()
        print(f" [x] Received: {code}")
        datos= code+" oscar gomez toledano 04864501"
        self.publicar('results', datos)
        
    def publicar(self,props,message):
        publish_connection = pika.BlockingConnection(self.parameters)
        publish_channel=publish_connection.channel()
        publish_channel.exchange_declare(exchange='result')
        properties= pika.BasicProperties(
            delivery_mode=1)
        publish_channel.basic_publish(exchange='result',routing_key=,body=message,properties=properties)
        publish_connection.close()
        print(f" [x] Sent: {message}")

client= App('localhost')