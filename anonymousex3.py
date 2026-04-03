def fdmix(lst):
    a=lst[0]
    for val in lst:
        if a<val:
            a=val
    return a
def fdmin(lst):
    s=lst[0]
    for val in lst:
        if s>val:
            s=val
    return s
lst=[10,20,3,40,0,-1]
res=fdmix(lst)
res1=fdmin(lst)
print('max={}'.format(res))
print('min={}'.format(res1))