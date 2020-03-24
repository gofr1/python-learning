#!/usr/bin/env python3

from math import pi

def main():
    seq = range(11)
    seq2 = [x *2 for x in seq]
    seq3 = [x for x in seq if x % 3 != 0]
    seq4 = [(x, x**2) for x in seq]
    seq5 = [round(pi, i) for i in seq]
    seq6 = {x for x in 'superduper' if x not in 'pd'}
    print_list(seq)
    print_list(seq2)
    print_list(seq3)
    print_list(seq4)
    print_list(seq5)
    print_list(seq6)

def print_list(o):
    for x in o: print(x, end=" ")
    print()

if __name__ == "__main__":
    main()