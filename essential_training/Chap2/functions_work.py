def is_prime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
        else:
            return True

def list_primes():
    for n in range(100):
        if is_prime(n):
            print(n, end = " ", flush= True)
    print()

is_prime(5)
is_prime(4)
list_primes()