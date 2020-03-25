#!/usr/bin/env python3

def main():
    s = 'This is a long string with a bunch of words in it.'
    print(s)
    print(s.split()) # split string in a list

    l = s.split()
    s2 = ':'.join(l)
    print(s2)

if __name__ == '__main__':
    main()