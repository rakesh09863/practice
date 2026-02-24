#program for arithmetic operations
while(True):
    try:
        print('\t1.Addition')
        print('\t2.subtraction')
        print('\t3.multiplication')
        print('\t4.division')
        print('\t5.floor division')
        print('\t6.modulo division')
        print('\t7.power')
        ch=int(input('enter the value:'))
        match(ch):
            case 1:
                a=int(input('enter the value:'))
                b=int(input('enter the value:'))
                print('sum({}+{})={}'.format(a,b,a+b))
                break
            case 2:
                a=int(input('enter the value:'))
                b=int(input('enter the value:'))
                print('sub({}-{})={}'.format(a,b,a-b))
                break
            case 3:
                a=int(input('enter the value:'))
                b=int(input('enter the value:'))
                print('mult({}*{})={}'.format(a,b,a*b))
                break
            case 4:
                a=int(input('enter the value:'))
                b=int(input('enter the value:'))
                if b==0:
                    print('zero division error don`t enter zero')
                else:
                    print('div({}/{})={}'.format(a,b,a/b))
                break
            case 5:
                a=int(input('enter the value:'))
                b=int(input('enter the value:'))
                if b==0:
                    print('zero division error don`t enter zero')
                else:
                    print('floordiv({}//{})={}'.format(a,b,a//b))
            case 6:
                a=int(input('enter the value:'))
                b=int(input('enter the value:'))
                if b==0:
                    print('zero division error don`t enter zero')
                else:
                    print('modulodiv({}%{})={}'.format(a,b,a%b))
            case 7:
                a=int(input('enter the value:'))
                b=int(input('enter the value:'))
                print('power({}**{})={}'.format(a,b,a**b))
            case _:
                print('invalid selection pls try again')
    except ValueError:
        print('don`t enter str values or spaces or special symbols')
