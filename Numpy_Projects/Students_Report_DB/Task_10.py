#find all the student names who scored higher than student 15 in both subject1 and subject 2
from Import_data import students_array
sub1 = students_array[1:,1].astype('int')
sub2 = students_array[1:,2].astype('int')
sub1_stud15 = students_array[15,1].astype('int')
sub2_stud15 = students_array[15,2].astype('int')
names = students_array[1:,0]
cond = (sub1>sub1_stud15) & (sub2>sub2_stud15)
print(names[cond])