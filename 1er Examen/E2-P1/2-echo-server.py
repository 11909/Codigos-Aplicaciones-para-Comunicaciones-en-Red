#!/usr/bin python3

'''import socket
HOST = "192.168.0.132"  # Direccion de la interfaz de loopback estándar (localhost)
PORT = 5005  # Puerto que usa el cliente  (los puertos sin provilegios son > 1023)
buffer_size = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    TCPServerSocket.bind((HOST, PORT))
    TCPServerSocket.listen()
    print("El servidor TCP está disponible y en espera de solicitudes")

    Client_conn, Client_addr = TCPServerSocket.accept()
    with Client_conn:
        print("Conectado a", Client_addr)
        while True:
            print("Esperando a recibir datos... ")
            data = Client_conn.recv(buffer_size)
            print ("Recibido,", data,"   de ", Client_addr)
            if not data:
                break
            print("Enviando respuesta a", Client_addr)
            Client_conn.sendall(data)
'''




import socket

HOST = "192.168.0.132"
PORT = 5005
buffer_size = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    TCPServerSocket.bind((HOST, PORT))
    TCPServerSocket.listen()
    print("Servidor TCP esperando conexión...")

    conn, addr = TCPServerSocket.accept()
    with conn:
        print("Conectado a:", addr)

        contador = 0
        while contador < 100:
            data = conn.recv(buffer_size)
            if not data:
                break
            contador += 1
            print(f"[{contador}] {data.decode()}")

    print("Servidor TCP cerró la conexión")

