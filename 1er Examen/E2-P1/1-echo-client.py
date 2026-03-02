#!/usr/bin python3
'''
import socket

HOST = "192.168.0.132"  # Hostname o  dirección IP del servidor
PORT = 5005  # Puerto del servidor
buffer_size = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    TCPClientSocket.connect((HOST, PORT))
    print("Enviando mensaje...")
    TCPClientSocket.sendall(b"Hola servidor TCP ")
    print("Esperando una respuesta...")
    data = TCPClientSocket.recv(buffer_size)
    print("Recibido,", repr(data), " de", TCPClientSocket.getpeername())
    '''
    
    
    
    #!/usr/bin/env python3
import socket
import time

SERVER_IP = "192.168.0.132"
SERVER_PORT = 5005
CLIENT_IP = "192.168.1.98"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    TCPClientSocket.connect((SERVER_IP, SERVER_PORT))

    for i in range(1, 101):
        mensaje = (
            f"El cliente TCP con la IP {CLIENT_IP} "
            f"y el puerto {SERVER_PORT} mandó el mensaje {i}"
        )
        TCPClientSocket.sendall(mensaje.encode())
        time.sleep(0.05)

    print("Cliente TCP terminó de enviar 100 mensajes")

