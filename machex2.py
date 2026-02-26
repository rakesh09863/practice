import sys
while(True):
    try:
        print('1.Circle')
        print('2.Square')
        print('3.Rectangle')
        print('4.Triangle')
        print('5.Exit')
        ch=int(input('enter the value:'))
        match(ch):
            case 1:
                a=int(input('enter the radius:'))
                if a<=0:
                    print('don`t enter the 0 or -ve values')
                else:
                    print('Area of a circle={}'.format(3.14*a**2))
            case 2:
                a=int(input('enter the side:'))
                if a<=0:
                    print('don`t enter the Zero or -ve values')
                else:
                    print('Area of a square={}'.format(a**2))
            case 3:
                a=int(input('enter the length:'))
                b=int(input('enter the width:'))
                if a<=0 or b<=0:
                    print('don`t enter the Zero or -ve value')
                else:
                    print('Area of rectangle={}'.format(a*b))
            case 4:
                a=int(input('enter the base value:'))
                b=int(input('enter the height value:'))
                if a<=0 or b<=0:
                    print('don`t enter the Zero or -ve values')
                else:
                    print('Area of Triangle={}'.format(1/2*a*b))
            case 5:
                print('Exit')
                sys.exit()
            case _:
                 print('Invalid input try again--')
        break
    except ValueError:
        print('Invalid input')