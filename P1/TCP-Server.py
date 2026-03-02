import socket 
import time 
 
HOST = "192.168.1.69" 
PORT = 5005 
bufferSize = 1024 
 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket: 
    serverSocket.bind((HOST, PORT)) 
    serverSocket.listen() 
    print("Servidor TCP activo, esperando conexión...") 
    conn, addr = serverSocket.accept() 
 
    with conn: 
        print(f"\nConectado con {addr}") 
 
        buffer="" 
        contador=0 
        inicio=time.time() 
 
        while True: 
            data = conn.recv(bufferSize).decode() 
 
            if not data: 
                break 
 
            buffer +=data 
 
            while "\n" in buffer: 
                linea, buffer =buffer.split("\n", 1) 
                contador+=1 
                print(f"Paquete recibido [{contador}]: {linea}") 
 
        fin = time.time() 
 
        print("\n===== MÉTRICAS SERVIDOR =====") 
        print(f"Total paquetes recibidos: {contador}") 
        print(f"Tiempo total: {fin - inicio:.4f} segundos") 
        if fin - inicio > 0: 
            print(f"Paquetes por segundo: {contador/(fin-inicio):.2f}")