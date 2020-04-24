#!/usr/bin/env python3

def even_integers_function(n):
    result = []
    for i in range(n):
        if i%2 == 0:
            result.append(i)
    return result

# a generator function returns a generator object
def even_integers_generator(n):
    for i in range(n):
        if i%2 == 0:
            yield i   

def main():
    print(even_integers_generator(10)) # returns generator object
    print(list(even_integers_generator(10))) #returns values

    print(even_integers_function(10))

    # use a generator object
    evenInt = even_integers_generator(10)

    print(f"The next element is: {next(evenInt)}") # 0
    print(f"if we print list after next it will show elements that was left: {list(evenInt)}") # 2, 4, 6, 8
    # next print(next(evenInt)) will throw 
    # StopIteration error
    # but for loophandles this
    # generator objects cannot be reused
    
    # iterate
    for n in even_integers_generator(10):
        print(n)
    
    for n in (n for n in range(10) if n%2 == 0):
        print(n)
    
    # some functions
    print(f"Max value from generator function: {max(even_integers_generator(10))}")
    # or
    print(f"Max value from generator: {max(n for n in range(10) if n%2 == 0)}")

if __name__ == '__main__':
    main()