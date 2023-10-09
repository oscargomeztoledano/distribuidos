#!/usr/bin/python3
import socket
import sys

try:
    msg=sys.argv[1]
    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
        s.sendto(msg.encode(),("localhost",1234))
        print("mensaje enviado")

except IndexError:
    print("Error, ponga el mensaje en el parametro 1")
