#Find the name and count of students where subject 1 marks is greater than subject 2 marks
from Import_data import students_array
name = students_array[1:,0]
sub1 = students_array[1:,1].astype('int')
sub2 = students_array[1:,2].astype('int')
print(name)
print(sub1)
print(sub2)
cond = sub1 > sub2
print(f'names of students whoes marks in sub1 are greater than sub2: {name[cond]}\n count of students whose marks in sub1 are greaterthan sub2: {len(name[cond])}')