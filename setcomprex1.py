lst=[10,20,-30,-40,50,60,-15,0,25]
pslist={val for val in lst if val>0}
nslist={val for val in lst if val<0}
zeroval={val for val in lst if val==0}
print('+ve values={}'.format(pslist))
print('-ve values={}'.format(nslist))
print('zero ={}'.format(zeroval))