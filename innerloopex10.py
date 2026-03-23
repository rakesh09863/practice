#Program for Generating List of Primes for n Random Dynamic Numbers where N is +Ve
while(True):
    try:
        a=int(input('enter the primes numbers:'))
        lst=[]
        for i in range(1,a+1):
            b=int(input('enter the value:'))
            lst.append(b)
        print(lst)
        for j in lst:
            res=True
            for k in range(2,j):
                if j%k==0:
                    res=False
                    break
            else:
                if res:
                    print(j)
        break
    except ValueError:
        print(' invalid pls try again')

