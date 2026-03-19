a='python'
i=0
while(i<len(a)):
    print(a[i])
    i+=1
print('-'*50)
while(i<len(a)):
    if a[i]=='o':
        i=i+1
        continue
    print(a[i])
    i+=1
