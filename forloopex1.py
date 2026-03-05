while(True):
    a=input('enter the value:').strip()
    if len(a)==0:
        print('don`t enter space try again---')
    elif not a.isdigit():
        print('don`t enter alphabits and -ve values pls try again')
    else:
        a=int(a)
        for val in range(1,a+1):
            print(val)
        break