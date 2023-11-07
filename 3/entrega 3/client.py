#!/usr/bin/python3

import factorial_pb2
import factorial_pb2_grpc
import sys
import grpc

port=4080

if len(sys.argv) < 2: 
    print('Usage: ./client.py <host>')
    exit()


channel = grpc.insecure_channel(f'{sys.argv[1]}:{port}')
stub = factorial_pb2_grpc.FactorialCheckerStub(channel)


request = factorial_pb2.NumberRequest(email="oscar.gomez9@alu.uclm.es")

response = stub.RequestRandomNumber(request)

print(response.number)

factorial = 1
i = 1
while (i <= response.number):
    factorial = factorial * i
    i = i + 1

print("El factorial de " + str(response.number) + " es " + str(factorial))

request2 = factorial_pb2.CheckRequest(email="oscar.gomez9@alu.uclm.es", factorial=factorial)

response2 = stub.CheckFactorial(request2)

print(response2.result)