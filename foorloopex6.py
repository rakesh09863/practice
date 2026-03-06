while(True):
    try:
        b=int(input('enter the value:'))
        if b<=0:
            print('invalid input try again--')
        else:
            a=b
            if a%2==0:
                a=a-1
            for val in range(a,0,-2):
                print(val)
            print('-'*50)
            y=b
            if y%2!=0:
                y=y-1
            for val in range(y,0,-2):
                print(val)
            break
    except ValueError:
        print('invalid input')