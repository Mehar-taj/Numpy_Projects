#find the subject avg of student 5 to student 14
from Import_data import students_array
stud_5_to_14 = students_array[5:15,1:].astype('int').mean(axis=0)
print(stud_5_to_14)
