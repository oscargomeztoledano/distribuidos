#!/usr/bin/python3

import socket
import struct
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind(("", 1234))
        print("servidor encendido esperando a recibir.")
        msg, addr = s.recvfrom(1024)
        legth_string, data = struct.unpack("!H"+str(len(msg)-2)+"s", msg)
        print(data.decode())