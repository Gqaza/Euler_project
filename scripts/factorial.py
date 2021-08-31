"""
n! means n × (n − 1) × ... × 3 × 2 × 1

Find the sum of the digits in the number 100!
"""

# %%
def factorial(x):
    x_ = [n for n in range(x,0,-1)]
    n_fact = 1

    for n in x_:
        n_fact *= n
    return n_fact

def dig_sum(n):
    sum_ = 0
    for digit in str(n):
        sum_ += int(digit)
    return sum_

# %%
f = factorial(100)
print(dig_sum(f))
# %%
