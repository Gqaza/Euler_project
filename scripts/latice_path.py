"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?

no. of possible routes == (2𝑛)/(!𝑛!𝑛!)
"""

# %%
import math 
def paths(n):
    n_fac = math.factorial(n)
    return int(math.factorial(2*n)/(n_fac*n_fac))
print(paths(20))
