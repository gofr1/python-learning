#!/usr/bin/env python3

# Function caching allows us to cache the return values of a function depending on the arguments. 
# It can save time when an I/O bound function is periodically called with the same arguments. 
# Before Python 3.2 we had to write a custom implementation. 
# In Python 3.2+ there is an lru_cache decorator which allows us to quickly cache and uncache 
# the return values of a function.

from functools import lru_cache 
import time 

# Function that computes Fibonacci numbers without lru_cache 
def fib_without_cache(n): 
    if n < 2: 
        return n 
    return fib_without_cache(n-1) + fib_without_cache(n-2) 
      
# Function that computes Fibonacci numbers with lru_cache 
@lru_cache(maxsize = 128) # The maxsize argument tells lru_cache about how many recent return values to cache.
def fib_with_cache(n): 
    if n < 2: 
        return n 
    return fib_with_cache(n-1) + fib_with_cache(n-2) 


if __name__ == '__main__':
    
    begin = time.time() # Execution start time 
    _ = fib_without_cache(33) 
    end = time.time() # Execution end time 
    
    without_cache_time = end-begin

    print(f'Time taken to execute the function w/o lru_cache is: {without_cache_time}') 
    
    begin = time.time() 
    _ = fib_with_cache(33) 
    end = time.time() 

    ci = fib_with_cache.cache_info() # showing hits, misses, maxsize and currsize. 
    #In a multi-threaded environment, the hits and misses are approximate.

    fib_with_cache.cache_clear() # for clearing or invalidating the cache

    with_cache_time = end-begin

    print(f'Time taken to execute the function w/ lru_cache is: {with_cache_time}') 
    print(f'Difference is: {without_cache_time-with_cache_time}')
    print(f'Cache info: {ci}')

    
# The results:
#* Time taken to execute the function w/o lru_cache is: 1.8492403030395508
#* Time taken to execute the function w/ lru_cache is: 3.8623809814453125e-05
#* Difference is: 1.8492016792297363
#* Cache info: CacheInfo(hits=31, misses=34, maxsize=128, currsize=34)
# So function with cache works faster in current condition
