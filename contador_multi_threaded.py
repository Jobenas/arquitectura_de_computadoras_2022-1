import time
from threading import Thread

CUENTA = 50000000

NUM_HILOS = 2
hilos = []

def cuenta(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    inicio = time.perf_counter()
    for i in range(NUM_HILOS):
        t = Thread(target=cuenta, args=(CUENTA/NUM_HILOS, ))
        t.start()
        hilos.append(t)

    for hilo in hilos:
        hilo.join()
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion: {fin - inicio} segundos")
