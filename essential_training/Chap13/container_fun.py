#!/usr/bin/env python3

def main():
    x = tuple(range(0, 5))
    print(x)

    print(sum(x))
    print(min(x))
    print(max(x))

    print(tuple(reversed(x)))
    
    print(any(x))
    print(all(x))

    y = tuple(range(6, 11))
    z = zip(x, y)
    for a, b in z:
        print(f'{a} - {b}')

    animals = ('cat', 'rabbit', 'dog', 'velociraptor')
    for i, v in enumerate(animals):
        print(f'{i}: {v}')

if __name__ == '__main__':
    main()