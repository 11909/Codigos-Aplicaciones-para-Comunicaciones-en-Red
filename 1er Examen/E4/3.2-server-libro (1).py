#!/usr/bin/python3
import socket
import time
import os

HOST = "192.168.1.92"
PORT = 65432
BUFFER_SIZE = 1024
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    TCPServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPServerSocket.bind((HOST, PORT))
    TCPServerSocket.listen()
    print("Servidor TCP en espera de conexión...")

    Client_conn, Client_addr = TCPServerSocket.accept()
    with Client_conn:
        print(f"Conectado a {Client_addr}")

        # 1) Recibir el tamaño del archivo
        filesize = int(Client_conn.recv(BUFFER_SIZE).decode())
        print(f"Tamaño esperado: {filesize} bytes")

        # 2) Confirmar al cliente que puede empezar
        Client_conn.send(b"inicia el envio")

        # 3) Recibir bloques y reconstruir archivo
        recvfile=0
        bloques=0
        inicio=time.time()

        with open("./MobyDick.txt", "wb") as f:
            while recvfile < filesize:
                data = Client_conn.recv(BUFFER_SIZE)
                if not data:
                    break
                f.write(data)
                recvfile += len(data)  
                bloques += 1
                print(f"Bloque {bloques} pesa {len(data)} bytes, paquetes enviados: {recvfile}/{filesize}")

        fin = time.time()
        duracion = fin-inicio

        print("\nEstadísticas:")
        print(f"Bloques recibidos : {bloques}")
        print(f"Bytes recibidos   : {recvfile}")
        print(f"Tiempo total      : {duracion:.2f} s")
        print(f"Throughput        : {recvfile/duracion/1024:.2f} KB/s")
        print("Transferencia completa.")