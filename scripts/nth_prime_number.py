# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

# %%
def nth_prime(n):
    i = 0
    max_ = int(1e9)
    for p in range(2,max_):
        isPrime = True
        for m in range(2,p):
            if p%m == 0:
                isPrime = False
                break
        if isPrime == True:
            i += 1
        if i == n:
            break
    return {'index': i, 'prime': p}

print(nth_prime(10001))
# %%
