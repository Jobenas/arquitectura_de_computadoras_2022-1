import time
import concurrent.futures
from threading import Lock

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = Lock()
    
    def update (self, name):
        print(f"Thread {name}, iniciando actualizacion")
        print(f"Thread {name} a punto de adquirir el candado")
        # with self._lock:
        self._lock.acquire()
        print(f"Thread {name} ha adquirido el candado")
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        self._lock.release()
        print(f"Thread {name} a punto de liberar el candado")
        print(f"Thread {name} ha liberado el candado")
        print(f"Thread {name} terminando actualizacion")


if __name__ == "__main__":
    workers = 2
    db = FakeDatabase()
    print(f"Valor inicial de la base de datos: {db.value}")
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        for index in range(workers):
            executor.submit(db.update, index)
    print(f"Valor final de la base de datos: {db.value}")