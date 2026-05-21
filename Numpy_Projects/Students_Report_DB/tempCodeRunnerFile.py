from Import_data import student_array
eng_avg = student_array[1:,2].astype('int')
print(eng_avg.mean())