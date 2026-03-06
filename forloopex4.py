while(True):
    try:
        a=int(input('enter the value:'))
        if a<=0:
            print('don`t enter -ve values or 0')
        for val in range(1,a+1):
            if val%2==0:
                val=-1
            else:
                print(val)
        break
    except ValueError:
        print('invalid input try again--')
