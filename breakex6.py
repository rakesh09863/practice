#vowel program
a=input('enter the value:').lower()
if a.isdigit():
    print('don`t enter numbers')
elif len(a)!=1:
    print('try again')
else:
    res='vowel'
    if a not in ['a', 'e', 'i', 'o', 'u']:
        res='not vowel'
    print('{} is {}'.format(a,res))