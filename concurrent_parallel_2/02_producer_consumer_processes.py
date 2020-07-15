#!/usr/bin/env python3

# threads for i/o
# processes for cpu

# import threading
import multiprocessing as mp
import queue
import time

# serving_line = queue.Queue(maxsize=5)
serving_line = mp.Queue(5)

def cpu_work(work_units):
    x = 0
    for _ in range(work_units * 1_000_000):
        x += 1

def soup_producer(serving_line):
    for i in range(20):
        serving_line.put_nowait(f'Bowl #{i}')
        print(f'Served Bowl #{i} - remaining capacity: {serving_line._maxsize-serving_line.qsize()}')
        time.sleep(0.2)
    serving_line.put_nowait('no more soup for you!')
    serving_line.put_nowait('no more soup for you!')

def soup_consumer(serving_line):
    while True:
        bowl = serving_line.get()
        if bowl == 'no more soup for you!':
            break
        print(f'Ate {bowl}')
        # time.sleep(0.3)
        cpu_work(4)

if __name__ == "__main__":
    for consumer in range(2):
        mp.Process(target=soup_consumer, args=(serving_line,)).start()
    mp.Process(target=soup_producer, args=(serving_line,)).start()
