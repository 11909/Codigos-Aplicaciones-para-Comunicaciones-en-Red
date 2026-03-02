servidor: 
 import socket 
 
HOST = "192.168.1.777" 
PORT = 54321 
bufferSize = 1024 
N_TOTAL = 100  # Total de paquetes que esperamos del cliente 
 
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as UDPServerSocket: 
    UDPServerSocket.bind((HOST, PORT)) 
    print(f"Servidor listo en el puerto {PORT}. Esperando {N_TOTAL} paquetes...") 
 
    # Set para guardar números de secuencia únicos (evita contar duplicados) 
    paquetes_recibidos = set() 
 
 
    while True: 
        data, address = UDPServerSocket.recvfrom(bufferSize) 
        mensaje = data.decode() 
         
        try: 
            # Extrae el número del texto "Mensaje X" 
            num_secuencia = int(mensaje.split()[-1]) 
            paquetes_recibidos.add(num_secuencia) 
            print(f"Recibido: {mensaje} de {address}") 
        except: 
            continue 
 
        # Al recibir el mensaje 100, disparamos el reporte técnico 
        if "100" in mensaje: 
            n_unicos = len(paquetes_recibidos) 
             
            # Detectamos qué números del 1 al 100 no llegaron 
            esperados = set(range(1, N_TOTAL + 1)) 
            faltantes = sorted(list(esperados - paquetes_recibidos)) 
             
            # Aplicamos la fórmula de la imagen: ((N_total - N_unicos) / N_total) * 100 
            perdida_porcentaje = ((N_TOTAL - n_unicos) / N_TOTAL) * 100 
 
            print("\n" + "="*45) 
            print("         REPORTE DE MÉTRICAS UDP") 
            print("="*45) 
            print(f"Paquetes Enviados (N_total): {N_TOTAL}") 
            print(f"Paquetes Recibidos Únicos (N_unicos): {n_unicos}") 
            print(f"Porcentaje de Pérdida Real: {perdida_porcentaje:.2f}%") 
            print(f"Secuencias que se perdieron: {faltantes if faltantes else 'Ninguna'}") 
            print("="*45 + "\n") 
             
            # Limpiamos para el siguiente experimento (30%, 60%, etc.) 
            paquetes_recibidos.clear()