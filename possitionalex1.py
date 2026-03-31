#Program for Demonstrating Possitional Arguments
#PossArgsEx1.py
def display_student_info(roll_num,stud,marks):
    print(roll_num,',',stud,',',marks)

print('Main program')
display_student_info(input('Enter the first value:'),input('Enter the second value:'),input('Enter the third value:'))
display_student_info(10,'rakes',80)
display_student_info(20,'ravi',99)
display_student_info(30,'Raju',88)