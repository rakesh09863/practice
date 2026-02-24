a=int(input('enter the value:'))
if a<=0:
    print('don`t enter -ve values and Zero')
elif a%5==0 and a%3==0:
    print('{} is a multiple of 3 and 5'.format(a))
elif a%5==0:
    print('{} is multiple of 5'.format(a))
elif a%3==0:
    print('{} is a multiple of 3'.format(a))
