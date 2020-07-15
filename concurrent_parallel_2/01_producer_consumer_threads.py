#!/usr/bin/env python3

import threading
import queue
import time

serving_line = queue.Queue(maxsize=5)

def soup_producer():
    for i in range(20):
        serving_line.put_nowait(f'Bowl #{i}')
        print(f'Served Bowl #{i} - remaining capacity: {serving_line.maxsize-serving_line.qsize()}')
        time.sleep(0.2)
    serving_line.put_nowait('no more soup for you!')
    serving_line.put_nowait('no more soup for you!')

def soup_consumer():
    while True:
        bowl = serving_line.get()
        if bowl == 'no more soup for you!':
            break
        print(f'Ate {bowl}')
        time.sleep(0.3)

if __name__ == "__main__":
    for consumer in range(2):
        threading.Thread(target=soup_consumer).start()
    threading.Thread(target=soup_producer).start()
