#vowel program
while(True):
    a=input('enter the value:').lower().strip()
    if len(a)==0:
        print('try again')
    elif a.isdigit():
        print('don`t enter numbers')
    else:
        res='not vowel'
        for val in a:
            if val in ['a', 'e', 'i', 'o', 'u']:
                res='vowel'
                break
        print('{} is {}'.format(a, res))
        break
