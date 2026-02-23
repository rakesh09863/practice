a=input('enter the word:')
if a==a[::-1]:
    print('{} is palindrome'.format(a))
if a!=a[::-1]:
    print('{} is not a palindrome'.format(a))
print('program is completed')
