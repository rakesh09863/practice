name=input('enter the name:').strip()
if len(name)==0:
    print('don`t enter the space')
elif name.isdigit():
    print('don`t enter the number')
else:
    res='valid'
    for names in name.split():
        if not names.isalpha():
            res='invalid'
            break
    if res=='valid':
        print('{} is valid'.format(name))
    else:
        print('{} is invalid'.format(name))
