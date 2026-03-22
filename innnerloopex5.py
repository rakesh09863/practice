i=1
while(i<5):
    print('-'*50)
    print('outer loop={}'.format(i))
    print('-'*50)
    for val in range(3,0,-1):
        print('inner loop={}'.format(val))
    else:
        print('out of inner loop')
    i=i+1