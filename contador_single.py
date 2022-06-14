import time

CUENTA = 50000000


def cuenta(n):
    while n > 0:
        if n % 10000000 == 0:
            print(f"cruce un multiplo de 10 millones de cuentas")
        n -= 1


if __name__ == '__main__':
    inicio = time.perf_counter()
    cuenta(CUENTA)
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion: {fin - inicio} segundos")
