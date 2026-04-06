print('Enter the List of values separated by space:')
old_sal=[float(val) for val in input().split() if float(val)>0]
print(old_sal)
new_sal=list(map(lambda sal:sal+sal*50/100,old_sal))
print(new_sal)#10 20 30 -1 -4 -3 20 4
print('Old sal \t new sal')
for k,v in zip(old_sal,new_sal):
    print('{}---->{}'.format(k,v))

