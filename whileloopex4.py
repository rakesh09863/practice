while(True):
    a=input('enter the value:')
    if not a.isdigit():
        print('don`t enter the alphabit or space')
    elif len(a)==0:
        print('don`t enter space')
    else:
        a=int(a)
        i=1
        while(i<=a):
            print('{}'.format(a))
            a=a-1
        else:
            print('program is completed')
        break