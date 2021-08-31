'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the 
digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it 
lexicographic order. The lexicographic permutations of 0, 1 and 2 are: 012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

# %%
from itertools import permutations 
n = 9
idx = 1000000
perm = permutations([x for x in range(n+1)]) 
list_ = []
for i in list(perm): 
    x = "".join([str(j) for j in i])
    list_.append(x)
list_.sort()
print(list_[idx-1])
