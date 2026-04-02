lst=[10,20,30,40,-35]
sqr={val:val**2 for val in lst if val>0}
print('\tNumber\tSquare')
for k,v in sqr.items():
    print('\t{}\t\t{}'.format(k,v))