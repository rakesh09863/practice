n=int(input('enter the value:'))
if n<=0:
    print('don`t the -ve value')
else:
    lst=[]
    for val in range(n):
        a = int(input('enter the value:'))
        lst.append(a)
    else:
        ps=0
        ns=0
        r=[]
        s=[]
        z=[]
        print(lst)
        for i in lst:
            if i>0:
                ps=ps+i
                r.append(i)
            elif i<0:
                ns=ns+i
                s.append(i)
            else:
                z.append(i)
        print(r)
        print(s)
        print(z)
        print('sum of +ve values={}'.format(ps))
        print('sum of -ve values={}'.format(ns))





