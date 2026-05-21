
from Import_data import students_array
sub_avg = students_array[1:,[1,3,4]].astype('int')
print('avg of subject 1,3,4 for all students:',sub_avg.mean(axis=0))