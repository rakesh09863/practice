s='python'
i=0
while(i<len(s)):
    print(s[i])
    i+=1
print('-'*50)
i=0
while(i<len(s)):
    if s[i]=='p' or s[i]=='o':
        i=i+1
        continue
    print(s[i])
    i=i+1