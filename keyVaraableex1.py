def stud_info(**vals):
    for key,val in vals.items():
        print('{}-->{}'.format(key,val))


print('Main Program')
stud_info(name='Rakesh',sno=30,marks=98)
stud_info(name='Raja',sno=20,marks=90)
stud_info(name='Gayi',rollnum=20,marks=80)
stud_info(name='shilpa',sno=22)