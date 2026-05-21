#Accessing the avg of maths
from Import_data import students_array
avg = students_array[1:,1].astype('int')# it will convert the string values in the array to integer values
print(avg.mean())