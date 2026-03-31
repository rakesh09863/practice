def increment():
    global a,b
    a=a+1
    b=b+1
def modify():
    global a,b
    a=a*2
    b=b*2
print('Main program')
a,b=10,20
print('Before increment of a ={}'.format(a))
print('Before increment of b ={}'.format(b))
increment()
print('After increment of a ={}'.format(a))
print('After increment of b ={}'.format(b))
modify()
print('Modify of a ={}'.format(a))
print('Modify of b ={}'.format(b))