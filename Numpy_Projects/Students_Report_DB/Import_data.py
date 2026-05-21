# Importing data from csv file using genfromtxt() function
import numpy as np
students_array = np.genfromtxt('2_DATA_SCIENCE/1_Numpy/6_Students_Report_DB/students_data.csv', delimiter=',', dtype='str')
