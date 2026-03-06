while(True):
    try:
        a=int(input('enter the value:'))
        if a<=0:
            print('invalid input try again--')
            continue
        for val in range(1,a+1):
            print(val)
        break
    except ValueError:
        print('invalid input try again')
