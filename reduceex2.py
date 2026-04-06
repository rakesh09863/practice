import functools
print('Enter the list of values separated by space:')
lst=[float(val) for val in input().split()]
sumop=functools.reduce(lambda a,b:a+b,lst)
print(sumop)