#program for accepting List of Existing Sal of Employees and
#Give 50% Hike to employees
#MapEx2.py
def hike(sal):
    return sal+sal*50/100
print('Enter the List of values separated by space:')
old_sal=[float(val) for val in input().split() if float(val)>0]
print(old_sal)#10 20 30 -1 -4 -3 20 4
new_sal=list(map(hike,old_sal))
print('old_sal\t new_sal')
for k,v in zip(old_sal,new_sal):
    print('{}--->{}'.format(k,v))
