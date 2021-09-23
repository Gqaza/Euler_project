# %%

def isPrime(n):
    if n == 1:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def quadratic_equation(n, a, b):
    return n**2 + a*n + b


def quad_primes_size(a, b, m, n):
    num_primes = 0
    for i in range(n, m + 1):
        q = quadratic_equation(i, a, b)
        if not isPrime(q):
            return num_primes
        num_primes += 1
    return num_primes


def maximum_no_primes(m, n):
    no_primes = 0
    for a in range(m):
        for b in range(n, 0, -1):

