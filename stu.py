while(True):
    cm=input('enter the marks:').strip()
    if len(cm)==0:
        print('don`t enter the space try again')
    elif cm.isalpha():
        print('don`t enter the alphabets')
    else:
        cm=int(cm)
        if cm>0 and cm<100:
            print('{} is cm marks'.format(cm))
            break
        else:
            print('invalid')
