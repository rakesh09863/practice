while(True):
    a=input('enter the value:').strip()
    if len(a)==0:
        print('don`t enter space')
    elif not a.isdigit():
        print('invalid output try again---')
    else:
        a=int(a)
        for val in range(2,a+1):
            if val%2!=0:
                val=-1
            else:
                print(val)
        break
