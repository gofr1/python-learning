#!/usr/bin/env python3

import threading
from concurrent.futures import ThreadPoolExecutor # useful for I/O bound tasks

def vegetable_chopper(vegetable_id):
    name = threading.current_thread().getName()
    print(f'{name} chopped vegetable {vegetable_id}')

if __name__ == '__main__':
    pool = ThreadPoolExecutor(max_workers=5)
    for vegetable in range(100):
        #threading.Thread(target=vegetable_chopper, args=(vegetable,)).start()
        pool.submit(vegetable_chopper, vegetable)
    pool.shutdown()