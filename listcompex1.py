lst=[10,20,-30,-40,50,60,-15,0,25]
pslist=[val for val in lst if val>0]
nglist=[val for val in lst if val<0]
zeroval=[val for val in lst if val==0]
print('List of +ve values={}'.format(pslist))
print('List of -ve values={}'.format(nglist))
print('Zero Values ={}'.format(zeroval))