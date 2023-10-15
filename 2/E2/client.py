#!/usr/bin/python3

import sys
import socket
import student_pb2
if len(sys.argv) < 2:
    print('Usage: ./client.py <host>')
    exit()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destination = (sys.argv[1], 2003)

reading = student_pb2.Student()
reading.name.extend(["Victor", "Centellas Castañares"])
reading.age = 20
reading.email ="victor.centellas@alu.uclm.es"


data = reading.SerializeToString()
sock.sendto(data, destination)
reading2= student_pb2.StudentACK()

data, address = sock.recvfrom(1024)
    
reading2.ParseFromString(data)
print("Student {1}".format(reading2,student_pb2.StudentACK.StudentDataOK.Name(reading2.data_ok) ))
sock.close()
