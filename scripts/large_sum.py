# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

# %%
with open('../data/large_sums.csv', 'r') as f:
    lines = f.readlines()
numbers =[int(e.strip()) for e in lines]

sum_ = 0
for row in numbers:
    sum_ += row 
print(str(sum_)[:10])
