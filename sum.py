while(True):
    try:
        a=int(input('enter the number:'))
        if a<=0:
            print('don`t enter -ve values')
        else:
            s=0
            for i in range(1,11):
                print(i*a)
                s = s + i * a
            print('-'*50)
            print(s)
            break
    except ValueError:
        print('invalid input try again--')