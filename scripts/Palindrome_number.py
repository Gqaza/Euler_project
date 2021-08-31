
#A palindromic number reads the same both ways. The largest palindrome made from 
# the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# %%
def PalindomeProduct(x):
    m = 0
    for i in range(x,0,-1):
        for j in range(x,0,-1):
            p = str(i*j)
            if p[::-1] == p:
                if int(p) > m:
                    m = int(p)
    return m

print(PalindomeProduct(999))
