import socket
import hashlib

SOCK_BUFFER = 1024

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_address = ('localhost', 5000)
    sock.bind(server_address)

    sock.listen(5)

    while True:
        print("Esperando conexion")

        try:
            conn, client_address = sock.accept()
        except KeyboardInterrupt:
            print("Usuario termino abruptamente el programa")
            break
        
        print(f"Recibi conexion de cliente {client_address}")

        try:
            data = conn.recv(SOCK_BUFFER)
            if data:
                print(f"Recibi {data}")
                conn.sendall(b'ACK')
        except KeyboardInterrupt:
            print("Usuario termino abruptamente el programa")
            break
        except Exception as e:
            print(f"Sucedio algo: {e}")
        finally:
            print("cliente cerro la sesion")
            conn.close()