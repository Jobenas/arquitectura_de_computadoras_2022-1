import socket
import time

SOCK_BUFFER = 1024

if __name__ == '__main__':
    datos = input("Escriba algo: ")

    inicio = time.perf_counter()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)

    print(f"Conectandonos a servidor {server_address[0]}, en puerto {server_address[1]}")
    sock.connect(server_address)

    try:
        print("Enviando datos")
        # sock.sendall(b'Hola Mundo')
        sock.sendall(datos.encode("utf-8"))
        inicio_recepcion = time.perf_counter()
        data = sock.recv(SOCK_BUFFER)
        fin_recepcion = time.perf_counter()
    except Exception as e:
        print(f"Sucedio algo: {e}")
    finally:
        print("Cerrando conexion")
        sock.close()

    fin = time.perf_counter()
    
    print(f"Recibi {data}, en {fin - inicio} segundos")
    print(f"Recepcion unicamente de data por el socket es: {fin_recepcion - inicio_recepcion}")