"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, 
the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this 
sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of 
two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be 
written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even 
though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than 
this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
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

def num_type(n):
    sum_divisors = sum(divisors(n))
    if sum_divisors < n:
        return 'deficient'
    elif sum_divisors == n:
        return 'perfect_number'
    else:
       return 'abundant'

def abundant_nums(n):
    ab_nums = []
    for n in range(1,n):
        ntype = num_type(n)
        if ntype == 'abundant':
            ab_nums.append(n)
    return ab_nums

def SumsOfAbundant(n):
    ab_nums = abundant_nums(n)
    records = []
    for a in ab_nums:
        for b in ab_nums[::-1]:
            sum_ = a + b 
            records.append(sum_)
    return set(records)


def SumsNoneAbundant(n):
    ab_sums = SumsOfAbundant(n)
    sum_non = 0
    for i in range(1, n):
        if i not in ab_sums:
            sum_non += i
    return sum_non

# %%
print(SumsNoneAbundant(28123))
