import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("", 1234))
    print("servidor encendido esperando a recibir.")
    s.listen(1)
    c1,addr1=s.accept()
    c2,addr2=s.accept()

    while True:
        #comunicación cliente 1
        datos1=c1.recv(1024)
        if not datos1:
            break
        c2.send(datos1)

        #comunicación cliente 2
        datos2=c2.recv(1024)
        if not datos2:
            break
        c1.send(datos2)

        #verificamos si quieren continuar
        if input("si desea salir escriba 'exit'")=="exit":
            break
    c1.close()
    c2.close()
    s.close()