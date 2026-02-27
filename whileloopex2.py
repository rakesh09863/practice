while(True):
    a=input('enter the value:')
    if len(a)==0:
        print('don`t enter the space')
    elif not a.isdigit():
        print('don`t enter alphabit or space')
    else:
        a=int(a)
        if a<=0:
            print('don`t enter the zero or -ve values')
        else:
            i=1
            while(i<=a):
                print('\t{}'.format(i))
                i=i+1
            else:
                print('program is completed')
        break
