import time, random


def funkcija(q):
    while True:
        time.sleep(0.2)
        x = random.randint(0, 1880)
        q.put(x)