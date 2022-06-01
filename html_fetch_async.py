import asyncio
import time

import aiohttp
from aiohttp import ClientSession


async def fetch_html(url: str, session: ClientSession, **kwargs) -> int:
    try:
        resp = await session.request(method="GET", url=url, **kwargs)
        resp.raise_for_status()

        return resp.status
    except Exception as e:
        return 404


async def main():
    f = open("urls.txt", "r")
    content = f.read()
    f.close()

    content = content.split("\n")

    async with ClientSession() as session:
        tasks = []
        for url in content:
            tasks.append(
                fetch_html(url, session)
            )
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    inicio = time.perf_counter()
    asyncio.run(main())
    fin = time.perf_counter()

    print(f"Todas las lecturas tomaron {fin - inicio} segundos")