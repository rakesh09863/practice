while(True):
    try:
        a=int(input('enter the value:'))
        if a<=0:
            print('don`t enter 0 or -ve values')
        else:
            i=1
            while(i<=a):
                print('{}'.format(a))
                a=a-1
            else:
                print('program is completed')
        break
    except ValueError:
        print('don`t enter the alphabit or space')