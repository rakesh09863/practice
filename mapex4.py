#program for adding Two List Elements
print('Enter the first value:')
a=[float(val) for val in input().strip() if float(val)>0]
print('Enter the second value:')
b=[float(val) for val in input().split() if float(val)>0]
c=list(map(lambda k,v:k+v,a,b))
for k,v,r in zip(a,b,c):
    print('sum({},{})={}'.format(a,b,c))