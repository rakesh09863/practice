i=5
while(i>=1):
    print('-'*50)
    print('outer loop={}'.format(i))
    print('-'*50)
    j=5
    while(j>=1):
        print('inner loop={}'.format(j))
        j=j-1
    else:
        print('out of inner loop')
    i=i-1