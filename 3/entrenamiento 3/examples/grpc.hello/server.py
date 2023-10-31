#!/usr/bin/python3
# This example is based on https://github.com/grpc/grpc/tree/v1.6.x/examples/python/helloworld

from concurrent import futures

import grpc
import hello_pb2
import hello_pb2_grpc


class Hello(hello_pb2_grpc.HelloServicer):
    def write(self, request, context):
        print("Client sent: '{}'".format(request.message))
        return hello_pb2.PrintReply()


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))    # diez hilos atendiendo peticiónes
hello_pb2_grpc.add_HelloServicer_to_server(Hello(), server) #añadimos el servicio al servidor
server.add_insecure_port('0.0.0.0:2000')    #puerto por el que escucha el servidor
server.start()  #ponemos el servidor en marcha


try:
    server.wait_for_termination()

except KeyboardInterrupt:
    server.stop(0)
