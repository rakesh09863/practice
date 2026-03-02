a=int(input('enter the N multiplication tables:'))
i=1
while(i<=a):
    print('-'*50)
    print('multiplication of {}'.format(i))
    print('-'*50)
    j=1
    while(j<=10):
        print('{}x{}={}'.format(i,j,i*j))
        j=j+1
    i=i+1