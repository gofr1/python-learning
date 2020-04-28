#!/usr/bin/env python3

def coroutine_decorator(func):
    def wrap(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return wrap

@coroutine_decorator
def counter(string):
    count = 0
    try:
        while True:
            item = yield
            if isinstance(item, str):
                if item in string:
                    count += 1
                    print(item)
                else:
                    print("No match")
            else:
                print("Not a string")
    except GeneratorExit:
        print(count) 

def main():
    c = counter('California')
    c.send('Cali')
    c.send('nia')
    c.send('Hawaii')
    c.send(1234)
    c.close()

if __name__ == '__main__':
    main()