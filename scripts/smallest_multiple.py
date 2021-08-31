"""
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of
the numbers from 1 to 20?
"""


def smallest_multiple(k):
    p = int(1e9)
    for n in range(k, p):
        i = 0
        for m in range(1, k + 1):
            if n % m > 0:
                break
            i += 1
        if i == k:
            break
    return (n)


# r = smallest_multiple(20)
# print(f"Result = {r}")
