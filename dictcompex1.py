lst=[10,20,30,40,-11,0,-5]
dict={val:val**2 for val in lst if val>0}
print('Numbers\tSquare')
for k,v in dict.items():
    print('\t{}\t{}'.format(k,v))