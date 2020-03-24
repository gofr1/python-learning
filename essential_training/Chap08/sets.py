#!/usr/bin/env python3

def main():
    # is like list but w/o duplicates
    a = set("abcdef") 
    b = set("defghi")
    print_set(a)
    print_set(b)
    print_set(a - b) # is in a but not in b
    print_set(a | b) # is in a or both sets
    print_set(a ^ b) # is in a or b but not in both sets
    print_set(a & b) # is in both sets

def print_set(o):
    print('{', end=' ')
    for x in o:
        print(x, end=' ')
    print('}')

if __name__ == "__main__":
    main()