# Finding avg marks of students in English
from Import_data import students_array
eng_avg = students_array[1:,2].astype('int')
print(eng_avg)
print(eng_avg.mean())