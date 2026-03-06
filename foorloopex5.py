while(True):
    try:
        a=int(input('enter the value:'))
        if a<=0:
            print('invalid input')
            continue
        for val in range(a,0,-1):
            print(val)
        break
    except ValueError:
        print('invalid try again--')