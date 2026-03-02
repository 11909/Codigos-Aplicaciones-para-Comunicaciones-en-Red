'''
import socket
HOST = "192.168.1.92"  # El hostname o IP del servidor
PORT = 5005  # El puerto usado por el servidor
msgFromClient = "Hola servidor UDP "
bytesToSend = str.encode(msgFromClient)
serverAddressPort = (HOST, PORT)
bufferSize = 1024

# Crea un socket UDP del lado del cliente

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as UDPClientSocket:
    # Enviando mensaje al servidor usando el socket UDP
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    print("Mensaje del servidor {}".format(msgFromServer[0]))
    UDPClientSocket.sendto(b'', serverAddressPort)
    
    '''
    
    
    #!/usr/bin/env python3
import socket
import time

SERVER_IP = "192.168.1.92"
SERVER_PORT = 5005
CLIENT_IP = "192.168.1.98"

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as UDPClientSocket:
    for i in range(1, 101):
        mensaje = (
            f"El cliente UDP con la IP {CLIENT_IP} "
            f"y el puerto {SERVER_PORT} mandó el mensaje {i}"
        )
        UDPClientSocket.sendto(mensaje.encode(), (SERVER_IP, SERVER_PORT))
        time.sleep(0.01)

    print("Cliente UDP terminó de enviar 100 mensajes")

