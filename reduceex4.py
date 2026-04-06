import functools
print('Enter the list value separated by comma:')
a=[val for val in input().split(',')]
line=functools.reduce(lambda k,v:k+' '+v,a)
print(line)