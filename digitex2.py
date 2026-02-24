d={0:'Zer0',1:'One',2:'Two',3:'Three',4:'Four',5:'five',6:'six',7:'siven',8:'eight',9:'nine'}
a=int(input('enter the value:'))
res=d.get(a) if d.get(a)!=None else '+ve number' if a>0 else '-ve number' if a<0 and a not in range(-1,-10,-1) else '-ve digit'
print(a,res)