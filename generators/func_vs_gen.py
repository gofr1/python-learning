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

if __name__ == '__main__':
    main()