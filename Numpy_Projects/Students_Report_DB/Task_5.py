#Finding avg of student_7 for 4 subjects 
from Import_data import students_array
st7 = students_array[7,1:5].astype('int')
print(st7)
print(st7.mean())