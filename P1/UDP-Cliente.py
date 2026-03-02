import socket 
import time 
 
SERVER_IP = "192.168.1.777"  
PORT = 54321 
 
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as UDPClientSocket: 
    print(f"Enviando ráfaga de 100 mensajes a {SERVER_IP}...") 
 
    for i in range(1, 101): 
        msg = f"Mensaje {i}" 
UDPClientSocket.sendto(msg.encode(), (SERVER_IP, PORT)) 
# Pausa mínima para que el sistema procese el envío 
time.sleep(0.01)  
print("¡Proceso de envío terminado!")