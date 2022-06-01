import asyncio
import time

async def cuenta(idx: int):
    print(f"[{idx}] Uno")
    await asyncio.sleep(1)
    print(f"[{idx}] Dos")


async def main():
    await asyncio.gather(cuenta(0), cuenta(1), cuenta(2))


if __name__ == "__main__":
    inicio = time.perf_counter()
    asyncio.run(main())
    fin = time.perf_counter()

    print(f"{__file__} ejecuto en {fin - inicio} segundos")