"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

Which starting number, under one million, produces the longest chain?
"""

# %%
def collatz_seq(n):
    seq_ = [n]
    while n > 1:
        if n % 2 == 0:
            n = int(n/2)
        else:
            n= 3*n + 1
        seq_.append(n)
    return seq_

# %%
x = 0
for i in range(1000000):
    len_ = len(collatz_seq(i))
    if len_ > x:
        x = len_
        start_ = i 
print(f'{start_} has the largest chain with {x} terms')
