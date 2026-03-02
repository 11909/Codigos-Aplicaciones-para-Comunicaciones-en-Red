#!/usr/bin/python3
import socket
import os
import time

HOST = "192.168.1.92"
PORT = 65432
BUFFER_SIZE = 1024
FILE_PATH = "./MobyDick.txt"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    TCPClientSocket.connect((HOST, PORT))
    print(f"Conectado al servidor {HOST}:{PORT}")

    # 1) Enviar tamaño del archivo
    filesize = os.path.getsize(FILE_PATH)
    print(f"Tamaño del archivo: {filesize} bytes")
    TCPClientSocket.sendall(str(filesize).encode())

    # 2) Esperar confirmación del servidor
    confirmacion = TCPClientSocket.recv(BUFFER_SIZE)
    print(f"Servidor dice: {confirmacion.decode()}")

    # 3) Enviar archivo en bloques
    bloques=0
    bytes_enviados=0
    inicio=time.time()

    with open(FILE_PATH, "rb") as archivo:
        while True:
            bloque = archivo.read(BUFFER_SIZE)
            if not bloque:          
                break
            TCPClientSocket.sendall(bloque)
            bloques += 1
            bytes_enviados += len(bloque) 

    fin = time.time()

    print("\nDatos del envio: ")
    print(f"Bloques enviados  : {bloques}")
    print(f"Bytes enviados    : {bytes_enviados}")
    print("Transferencia completa.")
    
    
    
