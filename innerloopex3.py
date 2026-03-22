i=1
while(i<6):
    print('-'*50)
    print('outer of loop={}'.format(i))
    print('-'*50)
    j=1
    while(j<6):
        print('inner loop={}'.format(j))
        j=j+1
    else:
        print('out of inner loop')
    i=i+1