#Finding the count of customers who has taken a personal loan
import numpy as np
from Bank_dataset import banking_array
personal_loan = banking_array[0:,4]=='yes'
print(np.count_nonzero(personal_loan))
