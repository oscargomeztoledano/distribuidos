#!/usr/bin/python3 -u
"Usage: {0} <host> <port>"

import sys
import socket
import struct
#192.168.8.134 1080

server_addr = (sys.argv[1], int(sys.argv[2]))


def deserialize_reading(data):
    color_len, = struct.unpack_from('f', data)
    color = data[4:4+int(color_len)].decode('utf-8')
    hour, minute, second = struct.unpack_from('ilh', data[4+int(color_len):])
    return color, hour, minute, second


if len(sys.argv) != 3:
    print(__doc__.format(__file__))
    sys.exit(1)

# FIXME: write your own UCLM ID
uclm_id = 'oscar.gomez9'  # if your email is John.Doe@alu.uclm.es

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Sending UCLM ID...')
msg = 'UID'.encode() + uclm_id.encode()
sock.sendto(msg, server_addr)

msg = sock.recv(1024)
reading = deserialize_reading(msg)

print('Sending result...')

mensaje=f'RES {reading[0].encode}{reading[1]}:{reading[2]}:{reading[3]}'
sock.sendto(mensaje, server_addr)
print('Server response: ', sock.recv(1024).decode())

sock.close()
