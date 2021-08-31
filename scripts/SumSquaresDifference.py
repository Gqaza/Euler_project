# Find the difference between the sum of the squares of the first one hundred natural numbers and 
# the square of the sum.

# %%
n = sum([x*x for x in range(1,101)])
m = sum([x for x in range(1,101)])
ans = m**2 - n
print(ans)
# %%
