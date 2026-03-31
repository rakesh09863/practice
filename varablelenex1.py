def stu_info(*vars):
    print(vars,type(vars),len(vars))

print('Main program')
stu_info(10,20,30,40,50)
stu_info(10,20,30,40)
stu_info(10,20,30)
stu_info(10,20)
stu_info(10)
stu_info()
stu_info(10,20,30,'ra','se')