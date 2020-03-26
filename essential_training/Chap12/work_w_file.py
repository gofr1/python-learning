#!/usr/bin/env python3

def main():
    # f is a file object and it is iterator
    f = open('lines.txt')
    for line in f:
        print(line.rstrip())
    f.close()

if __name__ == '__main__':
    main()