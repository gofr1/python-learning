#!/usr/bin/env python3

import threading
from concurrent.futures import ProcessPoolExecutor # useful for CPU bound tasks
import os

def vegetable_chopper(vegetable_id):
    #name = threading.current_thread().getName() # There always be MainThread (one of a five in this example)
    # so we switch to os module to get PID
    name = os.getpid()
    print(f'{name} chopped vegetable {vegetable_id}')

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=5) as pool: # this time lets use context manager
        for vegetable in range(100):
            pool.submit(vegetable_chopper, vegetable)
    # pool.shutdown()