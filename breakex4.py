a='mississippi'
i=0
ch=0
while(i<len(a)):
    if a[i]=='i':
        ch=ch+1
        if ch==2:
            break
    print(a[i],end='')
    i=i+1
