bval=lambda k,v: a if a>b else b if b>a else 'Both are Equal'
sval=lambda k,v:a if a<b else b if b<a else 'Both are Equal'
a=int(input('Enter the First value:'))
b=int(input('Enter the second value:'))
res=bval(a,b)
res1=sval(a,b)
print('max({},{})={}'.format(a,b,res))
print('min({},{})={}'.format(a,b,res1))