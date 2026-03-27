def sumop():
    a=float(input('enter the first value:'))
    b=float(input('enter the second value:'))
    c=a+b
    print('sum({}+{}={})'.format(a,b,c))
if __name__=="__main__":
    print('I am the main program')
    sumop()