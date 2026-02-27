while('t'):
    try:
        a=int(input('enter the value:'))
        if a<=0:
            print('don`t enter the Zero or -ve values')
        else:
            print('-'*50)
            print('Numbers within:{}'.format(a))
            print('-'*50)
            i=1
            while(i<=a):
                print('\t{}'.format(i))
                i=i+1
            else:
                print('-'*50)
                print('program is completed')
        break
    except ValueError:
        print('don`t enter space or alphabit try again--')