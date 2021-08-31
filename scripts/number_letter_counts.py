"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 
(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with 
British usage.
"""

# %%
words_u20 = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight',\
    9:'Nine', 10:'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',\
    15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}

words_tens = {2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety'}


def num2words(num):
    num_str = str(num)
    if num > 0 and num < 20:
        return words_u20[num]
    elif num >= 20  and num < 100:
        if  num_str[-1] == '0':
            word = words_tens[int(num_str[0])]
        else:
            word = f"{words_tens[int(num_str[0])]} {words_u20[int(num_str[-1])]}"

    elif num >= 100 and num < 1000:
        upper_bound = 'hundred'
        if num_str[-2:] == '00':
            word = f"{words_u20[int(num_str[0])]} {upper_bound}"
        elif int(num_str[-2:]) < 20:
            word = f'{words_u20[int(num_str[0])]} {upper_bound} and {words_u20[int(num_str[-2:])]}'
        elif num_str[-1] == '0' and num_str[-2] != '0':
            word = f'{words_u20[int(num_str[0])]} {upper_bound} and {words_tens[int(num_str[-2])]}'
        else:
            word = f'{words_u20[int(num_str[0])]} {upper_bound} and {words_tens[int(num_str[-2])]}-{words_u20[int(num_str[-1])]}'
    elif num == 1000:
        word = f'{words_u20[int(num_str[0])]} thousand'
    else:
        return ('This function can only convert numbers <= 1000')
    return word

# %%
letters_used = 0
for num in range(1,1001):
    num_word = num2words(num)
    word_stripped = num_word.replace(' ','').replace('-','')
    letters_used += len(word_stripped)
print(letters_used )
