#Finding the count of customers with personal loan and are married and has car loan
import numpy as np
from Bank_dataset import banking_array
personal_loan = banking_array[0:,4]=='yes'
married = banking_array[0:,2]=='married'
car_loan = banking_array[0:,5]=='yes'
cond = (personal_loan & married & car_loan)
print('the count of customers with personal loan and are married and has car loannp.count_nonzeros',np.count_nonzero(cond))