'''
The Fibonacci sequence is defined by the recurrence relation:
F_n = F_{n−1} + F_{n−2}, where F_1 = 1 and F_2 = 1.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''

# %%
def Fibonacci(n):
    seq = [1, 1]
    x = 0
    idx = len(seq)
    while len(str(x)) < n:
        x = seq[-1]+seq[-2]
        seq = seq[-1:]
        seq.append(x)
        idx += 1
    return idx

Fibonacci(1000)
