for val in range(1,6):
    print('-'*50)
    print('outer loop={}'.format(val))
    print('-'*50)
    i=1
    while(i<5):
        print('inner loop={}'.format(i))
        i=i+1
    print('outer inner loop')
