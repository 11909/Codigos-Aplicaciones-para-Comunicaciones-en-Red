import socket
import struct
import time

HOST = "0.0.0.0"
PORT = 5005
BUFFER_SIZE = 2048

UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPServerSocket.bind((HOST, PORT))

print("Servidor UDP activo, esperando archivo...")

file_chunks = {}
filename = None
total_expected = 0
start_time = 0

while True:
    data, address = UDPServerSocket.recvfrom(BUFFER_SIZE)

    if data.startswith(b"START:"):
        parts = data.decode().split(":")
        filename = parts[1]
        total_expected = int(parts[2]) # Guardamos el total esperado [cite: 43]
        file_chunks = {}
        start_time = time.time() # Iniciar cronómetro para throughput
        print(f"Recibiendo: {filename}. Paquetes esperados: {total_expected}")
        continue

    if data == b"END":
        end_time = time.time()
        total_received_unique = len(file_chunks) # Paquetes distintos [cite: 50]
        
        # --- Cálculo de Estadísticas ---
        duration = end_time - start_time
        # Fórmula de pérdida: (Total - Recibidos) / Total * 100 
        loss_percentage = ((total_expected - total_received_unique) / total_expected) * 100
        
        # Cálculo de bytes totales para throughput
        total_bytes = sum(len(c) for c in file_chunks.values())
        throughput = total_bytes / duration if duration > 0 else 0

        print("\n" + "="*30)
        print("RESUMEN DE TRANSMISIÓN UDP")
        print(f"Paquetes esperados: {total_expected}")
        print(f"Paquetes recibidos únicos: {total_received_unique}")
        print(f"Porcentaje de pérdida: {loss_percentage:.2f}%")
        print(f"Tiempo total: {duration:.4f} seg")
        print(f"Throughput: {throughput:.2f} bytes/seg")
        
        # Detección de secuencias faltantes 
        missing = [s for s in range(total_expected) if s not in file_chunks]
        if missing:
            print(f"Secuencias faltantes (primeras 10): {missing[:10]}")
        
        # Reconstrucción
        cadena_aux = "recibido_" + filename
        with open(cadena_aux, "wb") as f:
            for i in sorted(file_chunks.keys()):
                f.write(file_chunks[i])
        
        print("Archivo reconstruido. Saliendo...")
        break

    # Procesamiento de paquetes de datos
    seq = struct.unpack("!I", data[:4])[0]
    chunk = data[4:]
    file_chunks[seq] = chunk 
    # (Opcional: puedes mantener tus prints de resumen de chunk aquí)