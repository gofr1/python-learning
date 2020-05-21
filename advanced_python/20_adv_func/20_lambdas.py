#!/usr/bin/env python3

# lambdas are small anonymous functions
# can be passed as arguments where you need a function
# defined as: lambda (parameters) : (expression)

def CtoF(temp):
    return (temp*9/5)+32

def FtoC(temp):
    return (temp-32)*5/9

def main():
    ctemps = [0, 12, 34, 100]
    ftemps = [32, 65, 100, 212]

    # regular functions
    print(list(map(CtoF, ctemps)))
    print(list(map(FtoC, ftemps)))

    # lambdas
    print(list(map(lambda t: (t*9/5)+32, ctemps)))
    print(list(map(lambda t: (t-32)*5/9, ftemps)))
  
    c = lambda t: (t*9/5)+32
    print(list(map(c, ctemps)))

    f = lambda t: (t-32)*5/9
    print(list(map(f, ftemps)))

if __name__ == '__main__':
    main()