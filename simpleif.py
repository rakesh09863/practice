while(True):
    try:
        a=int(input('enter the number:'))
        if a>0:
            print('it is a +ve number')
        elif a<0:
            print('it is -ve number')
        else:
            print('Zero')
        break
    except ValueError:
        print('invalid input try again--')