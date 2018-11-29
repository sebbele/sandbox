#!/usr/bin/env python
import time

def update():
    start = time.time()

    # update every 1 second
    while True:
        now = time.time()
        if now - start > 1:
            print(now - start)
            start = time.time()

if __name__ == "__main__":
    update()
