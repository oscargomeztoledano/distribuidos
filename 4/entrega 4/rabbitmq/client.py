import pika

def callback(ch, method, properties, body):
    print("[x] Received: %r" % body.decode("UTF-8"))

credentials = pika.PlainCredentials('ssdd', 'student')
parameters = pika.ConnectionParameters(host='192.168.8.224', credentials=credentials)
connection = pika.BlockingConnection(parameters)

channel= connection.channel()
channel.queue_declare(queue='codes')

channel.basic_consumer(queue='codes', auto_ack=True, on_message_callback=callback)

print("[*] Waiting for messages. press Ctrl+C to exit")
channel.start_consuming()