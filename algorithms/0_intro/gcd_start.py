# find the greatest common denominator (GCD) of two numbers
# using Euclid's algorithm

def gcd(a, b):
    while (b != 0):
        t = a
        a = b
        b = t % a
    return a

gcd(12, 8)
gcd(60, 96)
