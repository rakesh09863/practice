even=lambda a:a>0
print('Enter the list of values separated by space:')
lst=[float(val) for val in input().split()]
pval=list(filter(even,lst))
print(pval)