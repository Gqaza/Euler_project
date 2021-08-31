"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called 
amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

# %%
def divisors(n):
    divisors = [1]
    for i in range(2,n):
        if i in divisors: 
            break
        if n % i == 0:
            divisors.append(i)
            divisors.append(int(n/i))
    return set(divisors)

def SumOfDivisors(n):
    return sum(divisors(n))

# %%
n = 10000
amic_sum = 0
for i in range(1,n):
    a = SumOfDivisors(i)
    for j in range(i+1, n):
        b = SumOfDivisors(j)
        if i == b and j == a:
            amic_sum += sum([i,j])
            print({i,j})
        if j >= a:
            break

# %%
