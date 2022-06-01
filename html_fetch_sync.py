import requests
import time

def fetch_url(url: str) -> int:
    resp = requests.get(url)

    return resp.status_code


def main():
    f = open("urls.txt", "r")
    content = f.read()
    f.close()

    content = content.split("\n")

    for url in content:
        status_code = fetch_url(url)


if __name__ == "__main__":
    inicio = time.perf_counter()
    main()
    fin = time.perf_counter()

    print(f"Todas las lecturas tomaron {fin - inicio} segundos")
