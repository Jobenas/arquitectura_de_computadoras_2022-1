import time
from threading import Thread

CUENTA = 50000000

def cuenta(n, name):
    while n > 0:
        # if n % 10000000 == 0:
        #     print(f"Estoy en el hilo: {name}")
        n -= 1


if __name__ == '__main__':
    t1 = Thread(target=cuenta, args=(CUENTA / 2, "hilo1"))
    t2 = Thread(target=cuenta, args=(CUENTA / 2, "hilo2"))

    inicio = time.perf_counter()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion: {fin - inicio} segundos")
