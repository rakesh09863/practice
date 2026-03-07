a='mississippi'
i=0
for val in a:
    if val=='s':
        i+=1
        if i==3:
            break
    print(val,end='')
