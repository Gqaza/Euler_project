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


def reciprocal_cycles(a, b):
    # list to store dict of current_value & remainder
    cvars = []
    current_value = a // b
    remainder = a % b
    subset = {f"{current_value}": remainder}
    while subset not in cvars:
        cvars.append(subset)
        current_value = remainder*10 // b
        remainder = remainder*10 % b
        subset = {f"{current_value}": remainder}
        if remainder == 0:
            return {"cycle": "", "len": 0}

    last_remainder = list(cvars[-1].values())[0]
    for dict_ in cvars[::-1][1:]:
        remainder = list(dict_.values())[0]
        if remainder == last_remainder:
            cycle_len = cvars[::-1][1:].index(dict_) + 1
            cycle = [
                list(x.keys())[0] for x in cvars[::-1][:cycle_len]
            ]
            cycle_str = ''.join(cycle)
            return {"cycle": cycle_str[::-1], "len": cycle_len}


def max_cycle(m):
    max_len = 0
    max_rc = {}
    for n in range(1, m):
        rc = reciprocal_cycles(1, n)
        if rc.get("len") > max_len:
            max_len = rc.get("len")
            max_rc = rc
            max_rc["denominator"] = n
    return max_rc


max_cycle(1000)
