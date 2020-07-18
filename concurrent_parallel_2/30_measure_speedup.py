#!/usr/bin/env python3

from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing as mp
import time

def seq_sum(lo, hi):
    '''Sequential implementation'''
    return sum(range(lo, hi))

def par_sum(lo, hi, pool=None):
    '''Parallel implementation'''
    if not pool:
        with ProcessPoolExecutor() as executor:
            futures = par_sum(lo, hi, pool=executor)
            return sum(f.result() for f in as_completed(futures))
    else:
        if hi - lo <= 10_000: # as a "tweak" lets decrease a threshold heere
            return [pool.submit(sum, range(lo, hi))]
        else:
            mid = (hi + lo) // 2
            left = par_sum(lo, mid, pool=pool)
            right = par_sum(mid, hi, pool=pool)
            return left + right

if __name__ == '__main__':
    NUM_EVAL_RUNS = 1
    SUM_VALUE = 100_000_000

    print('Evaluating Sequential implementation...')
    sequential_result = seq_sum(1, SUM_VALUE) # warm up
    sequential_time = 0

    for i in range(NUM_EVAL_RUNS):
        start = time.perf_counter()
        seq_sum(1, SUM_VALUE)
        sequential_time += time.perf_counter() - start
    sequential_time /= NUM_EVAL_RUNS

    print('Evaluating Parallel implementation...')
    parallel_result = par_sum(1, SUM_VALUE) # warm up
    parallel_time = 0

    for i in range(NUM_EVAL_RUNS):
        start = time.perf_counter()
        par_sum(1, SUM_VALUE)
        parallel_time += time.perf_counter() - start
    parallel_time /= NUM_EVAL_RUNS

    if sequential_result != parallel_result:
        raise Exception('sequential_result and parallel_result do not match.')
    print(f'Average Sequential time: {sequential_time*1000:.2f} ms')
    print(f'Average Parallel time: {parallel_time*1000:.2f} ms')
    print(f'Speedup: {sequential_time/parallel_time:.2f}')
    print(f'Efficiency: {100*(sequential_time/parallel_time)/mp.cpu_count():.2f} %')
