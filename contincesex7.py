#ContinueEx4.py
n=int(input("Enter How Many Values u have: "))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    lst=[] # empty List for adding values
    for i in range(1,n+1):
        value=float(input("Enter {} Value:".format(i)))
        lst.append(value)
    else:
        print("List of Values")
        print(lst) # [10.0, -20.0, 30.0, -40.0, 50.0]
        ps=0
        pslist=[]
        for val in lst:
            if(val<=0):
                continue
            ps=ps+val
            pslist.append(val)
        else:
            print("\tList of +Ve Values")
            print("\t",pslist)
            print("\tSum of +Ve Values=",ps)
            ns=0
            nglist=list()
            for val in lst:
                if(val>0):
                    continue
                ns=ns+val
                nglist.append(val)
            else:
                print("\tList of -Ve Values")
                print("\t",nglist)
                print("\tSum of -Ve Values=", ns)