#!/usr/bin/python3

import socket
import person_pb2
import sys

if len(sys.argv) < 2: 
    print('Usage: ./client.py <host>')
    exit()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destination = (sys.argv[1], 4080)

Person= person_pb2.Person()
Person.name = "Oscar Gomez Toledano"
Person.dni= 4864501
Person.email.append('oscar.gomez9')
Person.email.append('alu')
Person.email.append('uclm')
Person.email.append('es')
datos= Person.SerializeToString()
sock.sendto(datos, destination)
print("Datos enviados")

datos_respuesta= sock.recv(1024)
respuesta=person_pb2.Result()
respuesta.ParseFromString(datos_respuesta)
print(f'El resultado es: {respuesta}')
sock.close()

