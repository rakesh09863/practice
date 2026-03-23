while(True):
    a=input('enter the primes number:').strip()
    if len(a)==0:
        print('don`t enter the space try again--')
    elif a.isalpha():
        print('don`t enter the alphabets try again--')
    else:
        b=int(a)
        for num in range(2,b+1):
            res=True
            for i in range(2,num):
                if num%i==0:
                    res=False
                    break
            else:
                if res:
                    print('\t',num)
        break

