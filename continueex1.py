while(True):
    a=input('enter the value:').strip().lower()
    if len(a)==0:
        print('don`t the space pls try again--')
    elif a.isdigit():
        print('don`t enter the number pls try again--')
    else:
        i=0
        for val in a:
            if val=='s':
                i=i+1
                if i==2:
                    continue
            print(val)
    break

