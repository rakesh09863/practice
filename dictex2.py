a=int(input('Enter the value:'))
if a<=0:
    print('invalid input')
else:
    lst=[]
    for val in range(1,a+1):
        b=int(input('Enter the value:'))
        lst.append(b)
    print(lst)
    lst2={val:val**2 for val in lst if val>0}
    print('Number\tSquare')
    for k,v in lst2.items():
        print('\t{}\t\t {}'.format(k,v))