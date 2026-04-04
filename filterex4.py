print('Enter the list of values separated by comma:')
lst=[val for val in input().split()]
print('list of words',lst)#rakesh the madam inn the ss
pval=list(filter(lambda word:word[0]==word[-1] and word==word[::-1],lst))
print(pval)