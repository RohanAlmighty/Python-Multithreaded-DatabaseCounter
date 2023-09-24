import threading
import models
from database import engine
from counter_action import create_reset_counter, increment_counter, view_counter


def increment(lock: threading.Lock, increment_val: int) -> None:
    for _ in range(increment_val):
        with lock:
            increment_counter()


def main(number_of_threads: int = 5, increment_val: int = 100) -> None:
    models.Base.metadata.create_all(bind=engine)

    create_reset_counter()

    threads = []
    lock = threading.Lock()

    for _ in range(number_of_threads):
        x = threading.Thread(target=increment, args=(lock, increment_val))
        threads.append(x)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(view_counter())


if __name__ == "__main__":
    main(number_of_threads=5, increment_val=100)
