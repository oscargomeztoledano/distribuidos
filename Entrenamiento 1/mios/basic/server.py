#!/usr/bin/python3
import socket

while True:
    s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    s.bind(("",1234))
    print("servidor encendido esperando a recibir.")
    msg, addr= s.recvfrom(1024)
    try:
        print(msg.decode("ascii"))
    except UnicodeDecodeError:
        print("no se puede decodificar en ascii, decodificando con utf-8")
        print(msg.decode("utf-8"))