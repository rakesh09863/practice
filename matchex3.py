print('''1.Dec to Binary\n  Dec to Octal\n  Dec to Hexa''')
print('''\n2.Binary to Dec\n  Binary to Oct\n  Binary to Hexa''')
print('''\n3.Octal to Dec\n  Octal to Bin\n  Octal to hexa''')
print('''\n4.Hexa to Dec\n  Hexa to Bin\n  Hexa to Oct''')
ch=int(input('enter the value:'))
match (ch):
    case 1:
        a=int(input('enter the decimal number:'))
        print('bin({})={}'.format(a,bin(a)))
        print('oct({})={}'.format(a,oct(a)))
        print('hex({})={}'.format(a,hex(a)))
    case 2:
        a=input('enter the value 0b or 0B:')
        bv=int(a,2)
        print('dec({})={}'.format(a,bv))
        print('oct({})={}'.format(a,oct(bv)))
        print('hexa({})={}'.format(a,hex(bv)))
    case 3:
        a=input('enter the value 0o or 0O:')
        bv=int(a,8)
        print('dec({})={}'.format(a,bv))
        print('bin({})={}'.format(a,bin(bv)))
        print('hex({})={}'.format(a,hex(bv)))
    case 4:
        a=input('enter the value 0x or 0X')
        bv=int(a,16)
        print('dec({})={}'.format(a,bv))
        print('oct({})={}'.format(a,oct(bv)))
        print('bin({})={}'.format(a,bin(bv)))
    case _:
        print('invalid input')


