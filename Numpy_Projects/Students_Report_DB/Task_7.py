#find the student average of the first 10 students
from Import_data import students_array
stu = students_array[1:11,1:].astype('int')
print("Overall avg of students:",stu.mean())
print("Row wise avg of students:",stu.mean(axis=1))# axis=1 means row wise
print("Column wise avg of students:",stu.mean(axis=0))# axis=0 means column 