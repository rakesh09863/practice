while(True):
    a=input('enter the value:')
    if len(a)==0:
        print('don`t enter the space try again--')
    elif not a.isdigit():
        print('don`t enter the alphabites try again--')
    else:
        a=int(a)
        if a%2==0:
            a=a-1
        i=1
        while(i<=a):
            print(i)
            i=i+2
        break