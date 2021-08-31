'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with 
denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit 
recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

# %%
def reccurring_length(d, x):
    first_entry = x[2]
    i = 1
    len_ = 0
    try:
        for i, char in enumerate(str(x)):
            if i>2:
                if first_entry != char and first_entry != str(x)[-1]:
                    len_ += 1
                    
                else:
                    upper_bound = 3 + len_
                    deg_ = x[2: upper_bound]
                    return {"digit": d, "rec_deg": deg_, "cycle_size": len_ + 1 }
    except IndexError as error:
        return None


def rec(d):
    x = str(1/d)

    for char in x[2:]:
        J = reccurring_length(d, x)
        if  J is not None:
            return J
        else:
            idx = x.find(char)
    return "No recurring cycle"


#%%
def longest_rec_cycle(n):
    longest_cycle = {"digit": None,'rec_deg': '', 'cycle_size': 0}
    for i in range(1,n + 1):
        y = rec(i)
        if type(y) == dict:
            if longest_cycle.get('cycle_size') <= y.get('cycle_size'):
                longest_cycle = y 
                
    return longest_cycle






    



        


    



# %%
