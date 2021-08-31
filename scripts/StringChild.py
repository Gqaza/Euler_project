#%%
s1 = 'ABCXZ'
s2 = 'BDIXJJZZ'


def drop_uncommon_chars(s1, common_chars):
    s11 = s1
    s1_idxs = []

    for idx,x in enumerate(s1):
        if x not in common_chars:
            s11=s11.replace(x,'')
        else:
            s1_idxs.append(idx)
    return {'string':s11, 'indexes':s1_idxs}


def common_charectors(s1, s2):
    if s1 == s2:
        return s1

    common_chars  = set.intersection(set(s1),set(s2))

    s11 = drop_uncommon_chars(s1,common_chars)
    s22 = drop_uncommon_chars(s2, common_chars)        
    
    return {'s1':s11, 's2':s22}

# %%
def string_child(s1,s2):
    k = common_charectors(s1, s2)
    s_1 = k['s1']['string']
    s_2 = k['s2']['string']

    z1 = ''
    z2 = ''

    for x in s_1:
        for j,y in enumerate(s_2):
            if x==y 
            and (z1 + x) in s_1 
            and ( (z2 +y) in s_2 or z2 + s_2[j-1] + x in s_2):
                z1=z1 + x
                z2=z2 + y

    return (z1,z2)
# %%
