def dispaly(a):
    print('type of obj={}'.format(type(a)))
    if type(a)==dict:
        for key,value in a.items():
            print('{}-->{}'.format(key,value))
    else:
        for val in a:
            print(val)
        print('-'*50)

lst=[10,20,'rake','raju']
dispaly(lst)
set={20,30,'ss','ww'}
dispaly(set)
tuple=(12,2,'rrs','T')
dispaly(tuple)
d={10:'rakesh',20:'raju',30:'rr'}
dispaly(d)

