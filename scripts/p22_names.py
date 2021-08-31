"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand 
first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for 
each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

# %%
alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',\
    'R','S','T','U','V','W','X','Y','Z']

with open('../data/names.txt', 'r') as file_:
    f = file_.read()
    names = list(eval(f))
names.sort()

def alpha_value(name):
    sum_ = 0
    for char in name:
        sum_ += alphabets.index(char) + 1
    return sum_

def name_score(name):
    idx = names.index(name) + 1
    return alpha_value(name) * idx


total_score = 0
for name in names:
    total_score += name_score(name)

