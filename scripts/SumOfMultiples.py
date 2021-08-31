# if we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def SumOfMultiples(x,y,k):
    multiples_x = [n for n in range(1,k) if n%x == 0]
    multiples_y = [m for m in range(1,k) if m%y == 0]

    z = set(multiples_x + multiples_y)
    return sum(z)

z = SumOfMultiples(3,5,1000)
print(z)


