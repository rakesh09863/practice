while(True):
    try:
        a=int(input('enter the value:'))
        if a<=0:
            print('don`t enter the zero or -ve')
        else:
            if a%2!=0:
                a=a-1
            i=2
            while (i <= a):
                    print(i)
                    i=i+2
            break
    except ValueError:
        print('don`t enter the alphabit or space')
