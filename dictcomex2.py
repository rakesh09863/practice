while(True):
    try:
        a=input('Enter the number of values you need:')
        if not a.isdigit():
            print('Invalid input try again--')
        else:
            a=int(a)
            if a<=0:
                print('Invalid input try again--')
            else:
                lst=[]
                for val in range(1,a+1):
                    a=int(input('Enter the value:'))
                    lst.append(a)
                dict={val:val**2 for val in lst if val>0}
                print('Normal\tSquare')
                for k,v in dict.items():
                    print('{}\t{}'.format(k,v))
                break
    except ValueError:
        print('Don`t enter invalid input')
