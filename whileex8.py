a=int(input('enter the  value:'))
print('-'*50)
print('multiplication table for {}'.format(a))
print('-'*50)
i=1
while(i<=10):
    print('{}x{}={}'.format(a,i,a*i))
    i=i+1