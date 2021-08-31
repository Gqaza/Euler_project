# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
# For example: 3^2 + 4^2 == 9 + 16 == 25 == 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# %%
import numpy as np
def hypotenus(a,b):
    return np.sqrt(a*a + b*b)

x = 1000 # sum(abc)
def prod_abc(x):
    c = 1
    prod = 0
    for a in range(2,x-3):
        for b in range(a+1,x-2):
            constraints = x - (a+b)
            c = hypotenus(a,b)
            if  constraints == c and c > b:
                prod = np.prod([a,b,c])
                break
        if prod > 0:
            break
    return f"prod({a},{b},{c}) = {prod}"
print (prod_abc(1000))
