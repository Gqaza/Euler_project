# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import numpy as np

def prime_lessthan_x(k):
    primes_k = []
    for p in range(2, k+1):
        isPrime = True
        for n in range(2,p):
            if p%n == 0:
                isPrime = False
        if isPrime:
            primes_k.append(p)
    return primes_k

def isPrime(k):
    for p in range(1, k+1):
        check_ = True
        for n in range(2,p):
            if p%n == 0:
                check_ = False
    return check_

def prime_factors(z):
    primes_k = set(prime_lessthan_x(11000))
    factors = []
    for p in primes_k:
        if p > 1:
            m = p
            while z % p == 0:
                factors.append(p)
                z = z / p
    return factors

print(prime_factors(600851475143)) # np.product(prime_factors(600851475143))