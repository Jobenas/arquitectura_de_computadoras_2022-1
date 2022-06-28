import time
from multiprocessing import Pool, cpu_count

CUENTA = 100000000

num_proc = 7

def cuenta(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    inputs = [CUENTA / num_proc for _ in range(num_proc)]
    p = Pool(processes=cpu_count() - 1)

    inicio = time.perf_counter()
    res = p.map(cuenta, inputs)
    p.close()
    p.join()
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion para {num_proc} procesos: {fin - inicio} segundos")

