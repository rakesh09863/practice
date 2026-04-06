#program for accepting List of Numerical values and Find their sum by using reduce()
#ReduceFunEx1.py
import functools
def sumop(k,v):
    return k+v
print('Enter the list of values separated by space:')
lst=[float(val) for val in input().split()]
print(lst)
sumval=functools.reduce(sumop,lst)
print(sumval)