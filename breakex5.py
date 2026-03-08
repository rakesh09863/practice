while(True):
    try:
        a=int(input('enter the value:'))
        if a<=1:
            print('invalid input try again--')
        else:
            res='Prime'
            for val in range(2,a):
                if a%val==0:
                   res='not prime'
                   break
            print('{}'.format(res))
            break
    except ValueError:
        print('don`t enter alphabit')