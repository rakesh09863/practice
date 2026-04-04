print('Enter the List of values separated by space:')
old_sal=[float(val) for val in input().split() if float(val)>0]
print(old_sal)
new_sal=list(map(lambda sal:sal+sal*50/100,old_sal))
print(new_sal)
print('Old sal \t new sal')
for k,v in zip(old_sal,new_sal):
    print('{}---->{}'.format(k,v))

