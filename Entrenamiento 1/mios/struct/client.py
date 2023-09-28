#!/usr/bin/env python3

import socket
import struct
import random
import string

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    sever=('localhost', 1234)
    length_string= random.randint(1, 10)
    data= ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=length_string))
    mensaje= struct.pack('!H'+str(length_string)+'s', length_string, data.encode())
    print(data)
    s.sendto(mensaje, sever)
    
