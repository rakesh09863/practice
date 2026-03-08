while(True):
    a=input('enter the value:').lower()
    if a.isdigit():
        print('don`t enter digits')
    elif len(a)==0:
        print('don`t enter space')
    else:
        res='not vowel'
        for i in a:
            if i in ['a','e','i','o','u']:
                res='vowel'
                break
        print('{} is {}'.format(a,res))
        break