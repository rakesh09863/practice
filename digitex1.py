while(True):
    a=input('enter the value:')
    try:
        a=int(a)
        if a==0:
            print('Zero')
        elif a==1:
            print('One')
        elif a==2:
            print('Two')
        elif a==3:
            print('Three')
        elif a==4:
            print('Four')
        elif a==5:
            print('Five')
        elif a==6:
            print('six')
        elif a==7:
            print('seven')
        elif a==8:
            print('eight')
        elif a==9:
            print('nine')
        elif a>=10:
            print('{} is number'.format(a))
        elif a in[-1,-2,-3,-4,-5,-6,-7,-8,-9]:
            print('{} is number'.format(a))
        elif a<=-10:
            print('{} is digit'.format(a))
        else:
            print('program is completed')
        break
    except ValueError:
        print('invalid input try again')