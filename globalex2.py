def increment():
    global a
    a=a+1
def modify():
    global a
    a=a*2
print('Main program')
a=10#Global variable
print('Before Increment',a)
increment()
print('After Increment {} '.format(a))
modify()
print('Modify number={}'.format(a))

