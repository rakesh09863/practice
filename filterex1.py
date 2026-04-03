def pos(a):
    if a>0:
        return True
    else:
        return False
def neg(a):
    if a<0:
        return True
    else:
        return False
print('Enter the value separated by comma:')
lst=[float(val) for val in input().split()]
print(lst)#10 20 -11 2 -3 -5 2 4 9 -3
fobj=list(filter(pos,lst))
fobj1=list(filter(neg,lst))
print('Positive numbers',fobj)
print('Negative number ',fobj1)
