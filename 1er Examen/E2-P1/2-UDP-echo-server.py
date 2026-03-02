'''
import socket

HOST = "192.168.0.132"  # El hostname o IP del servidor
PORT = 5005  # El puerto que usa el servidor
bufferSize = 1024
msgFromServer = "Hola cliente UDP"
bytesToSend = str.encode(msgFromServer)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as UDPServerSocket:
    UDPServerSocket.bind((HOST, PORT))

    print("Servidor UDP activo, esperando peticiones")
    # Listen for incoming datagrams
    msgFromServer = "Hola cliente UDP"

    bytesToSend = str.encode(msgFromServer)
    while (True):
        data, address = UDPServerSocket.recvfrom(bufferSize)
        if not data:
            break
        print("Mensaje del cliente:{}".format(data))
        print("Ip del cliente:{}".format(address))

        # Enviando una respuesta al cliente
        UDPServerSocket.sendto(bytesToSend, address)
'''

#!/usr/bin/env python3
import socket

HOST = "192.168.0.132"
PORT = 5005
bufferSize = 1024

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as UDPServerSocket:
    UDPServerSocket.bind((HOST, PORT))
    print("Servidor UDP activo...")

    contador = 0
    while contador < 100:
        data, address = UDPServerSocket.recvfrom(bufferSize)
        contador += 1
        print(f"[{contador}] {data.decode()}")

    print("Servidor UDP recibió 100 mensajes y finalizó")
