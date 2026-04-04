#hike the salary 50%
def new_sal(sal):
    return sal+sal*50/100
print('Enter the list of values separated by space:')
old_sal=[int(val) for val in input().split() if float(val)>0]
print(old_sal)#10 20 30 40
x=list(map(new_sal,old_sal))
print(x)