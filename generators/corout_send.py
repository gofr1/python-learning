#!/usr/bin/env python3

from corout_decorator import coroutine_decorator

def sender(filename, target):
    for line in open(filename):
        target.send(line)
    target.close()

@coroutine_decorator
def match_counter(string):
    count = 0
    try:
        while True:
            line = yield
            if string in line:
                count += 1
    except GeneratorExit:
        print('{} {}'.format(string, count))

@coroutine_decorator
def longer_then(n):
    count = 0
    try:
        while True:
            line = yield
            if len(line) > n:
                print(line)
                count += 1
    except GeneratorExit:
        print('Longer than {}: {}'.format(n, count))    


def main():
    c = match_counter("Sa")
    sender("names.txt", c)

    l = longer_then(16)
    sender("names.txt", l)

if __name__ == '__main__':
    main()