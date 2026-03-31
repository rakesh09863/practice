def stud_info(sno,name,marks,cources='Python'):
    print('{}\t\t{}\t{}\t{}'.format(sno,name,marks,cources))


print('Main program')
print('Rol_Num\tName\tMarks\tcources')
print('-'*50)
stud_info(sno=10,marks=98,name='Rakesh')
stud_info(marks=100,sno=20,name='Shilpa')
stud_info(name='Gayi',sno=40,marks=100)