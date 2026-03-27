def sumop():
    k=float(input('enter the first value:'))
    v=float(input('enter the second value:'))
    c=k+v
    return k,v,c
if __name__=="__main__":
    print('I am the main program')
res=sumop()
print('Sum({}+{}={})'.format(res[0],res[1],res[2]))