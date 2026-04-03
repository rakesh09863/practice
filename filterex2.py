def pos(a):
    return a>0
print('Enter the values separated by comma:')
lst=[float(val) for val in input().split()]
print(lst)#10 30 9 0 -4 -5 -6 7 8
fobj=list(filter(pos,lst))
print(fobj)