import socket 
import time 
 
HOST = 192.168.1.69   
PORT = 5005 
TOTAL = 100 
 
print(fConectando al servidor {HOST} y puerto {PORT}...) 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket 
    clientSocket.connect((HOST, PORT)) 
    print(fConectado al servidor {HOST}{PORT}n) 
 
    inicio = time.time() 
 
    for i in range(1, TOTAL + 1) 
        mensaje = f[{i}] Paquete TCP enviado desde 
{clientSocket.getsockname()[0]}{clientSocket.getsockname()[1]} 
        print(fEnviando paquete [{i}]) 
        clientSocket.sendall((mensaje + n).encode()) 
        time.sleep(0.01) 
 
    fin = time.time() 
 
    print(n===== MÉTRICAS CLIENTE =====) 
    print(fTotal paquetes enviados {TOTAL}) 
    print(fTiempo total envío {fin - inicio.4f} segundos) 
    if fin - inicio  0 
        print(fPaquetes por segundo {TOTAL(fin-inicio).2f})