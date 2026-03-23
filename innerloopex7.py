while(True):
    try:
        a=int(input('enter the value:'))
        if a<=0:
            print('don`t enter the -ve values or Zero')
        else:
            for i in range(1,a+1):
                print('-'*50)
                print('multiplication table of {}'.format(i))
                print('-'*50)
                for j in range(1,11):
                    print('{}*{}={}'.format(i,j,i*j))
            break
    except ValueError:
        print('don`t enter the alphabets or space')