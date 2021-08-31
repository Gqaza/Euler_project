# Find the sum of all the primes below two million.
# %%
import numpy as np

# Below is a simple but computationally intensive algorithm 
# Note, we checking n-2 numbers here 
def SumOfPrimes(n):
    sum_ = 0
    for p in range(2,n):
        isPrime = True
        for idx in range(2,p):
            if p % idx == 0:
                isPrime = False
                break
        if isPrime == True:
                sum_ = sum_ + p
    return sum_

# This algorithm uses the max divider trick which reduces e numbers we checking by half (n-2)/2
def isPrime(n):
    if n <= 1:
        return False
 
    max_div = np.floor(np.sqrt(n))
    for i in range(2, int(max_div)+1):
        if n % i == 0:
            return False
    return True


def SumOfPrimes_(n):
    sum_ = 0
    for p in range(2,n):
        if isPrime(p) == True:
            sum_ += p
    return sum_
