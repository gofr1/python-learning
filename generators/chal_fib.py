#!/usr/bin/env python3

def fibonacci_gen():
    trailing, lead = 0, 1
    while True:
        yield lead
        trailing, lead = lead, trailing + lead

def main():
    fib = fibonacci_gen()

    for _ in range(10):
        print(next(fib))

if __name__ == '__main__':
    main()