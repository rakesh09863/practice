while(True):
    try:
        a=int(input('enter the value:'))
        lst=[]
        for i in range(1,a+1):
            b=int(input('enter the first value:'))
            lst.append(b)
        else:
            print(lst)
            for j in lst:
                print('-'*50)
                print('multiplication of {}'.format(j))
                print('-'*50)
                if j<=0:pass
                else:
                    for k in range(1,11):
                        print('{}*{}={}'.format(j,k,j*k))
        break
    except ValueError:
        print('don`t enter the alphabets or space')




