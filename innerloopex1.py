for i in range(1,6):
    print('-'*50)
    print('out loop ={}'.format(i))
    print('-'*50)
    for j in range(1,6):
        print('inner loop={}'.format(j))
    else:
        print('out of inner loop')
