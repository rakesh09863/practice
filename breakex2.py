a='mississippi'
i=0
crt=0
while(i<len(a)):
    if a[i]=='p':
        crt+=1
        if crt==2:
            break
    print(a[i])
    i=i+1
else:
    print(a[i],end='')
