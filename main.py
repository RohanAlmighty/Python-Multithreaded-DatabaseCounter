import threading
import models
from database import engine
from counter_action import create_reset_counter, increment_counter, view_counter

models.Base.metadata.create_all(bind=engine)

lock = threading.Lock()

create_reset_counter()


def increment():
    for _ in range(100):
        with lock:
            increment_counter()


threads = []
for i in range(5):
    x = threading.Thread(target=increment)
    threads.append(x)

for t in threads:
    t.start()

for t in threads:
    t.join()

print(view_counter())
