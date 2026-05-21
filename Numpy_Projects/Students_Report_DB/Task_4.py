# Finding the avg of student 7
from Import_data import students_array
st7_marks_avg = students_array[7,1:].astype('int')
print(st7_marks_avg.mean())