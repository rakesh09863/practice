a=10
b=20
c=30
d=40
def operation():
    k=10
    v=20
    z=30
    y=40
    global a,b,c,d
    res=k+v+z+y+a+b+c+d
    print('Result=',res)
print('Main program')
operation()