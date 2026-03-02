import socket
import os
import struct

SERVER_HOST = "192.168.0.132"
SERVER_PORT = 5005
BUFFER_SIZE = 1024
CHUNK_SIZE = 1000  # dejamos espacio para encabezado

file_path = "MobyDick.txt"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enviar nombre del archivo primero
filename = os.path.basename(file_path)
sock.sendto(f"START:{filename}".encode(), (SERVER_HOST, SERVER_PORT))

seq = 0

with open(file_path, "rb") as f:
    while True:
        chunk = f.read(CHUNK_SIZE)
        if not chunk:
            break
        
        # Empaquetamos número de secuencia (4 bytes) + datos
        packet = struct.pack("!I", seq) + chunk
        sock.sendto(packet, (SERVER_HOST, SERVER_PORT))
        seq += 1

# Mensaje de finalización
sock.sendto(b"END", (SERVER_HOST, SERVER_PORT))

print("Archivo enviado correctamente.")
sock.close()
