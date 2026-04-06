#program for accepting List of Numerical values and Find max and min by using reduce()
import functools
print('Enter the list of value separated by space:')
lst=[float(val) for val in input().split()]
print(lst)
maxop=functools.reduce(lambda k,v:k if k>v else v,lst)
minop=functools.reduce(lambda k,v:k if k<v else v,lst)
print('max of value={}'.format(maxop))
print('min of value={}'.format(minop))
