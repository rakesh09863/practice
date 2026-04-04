def prime(a):
    res=True
    for i in range(2,a):
        if(a%i)==0:
            res=False
            break
    return res
print('Enter the List of values separated by comma:')
lst=[int(val) for val in input().split() if int(val)>0]
print(lst)
plist=list(filter(prime,lst))
print(plist)