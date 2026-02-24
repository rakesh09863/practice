while(True):
    a=input('enter the value:')
    if len(a)==0:
        print('don`t enter space')
    elif a.isalpha():
        print('don`t enter alphabit')
    else:
        a=int(a)
        if a<=0:
            print('don`t enter zero or -ve values')
        else:
            s=0
            for i in range(1,11):
                s = s + a * i
                print(i)
            print('-'*50)
            print(s)
            break


