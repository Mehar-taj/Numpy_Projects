import numpy as np
from Bank_dataset import banking_array
personal_loan = banking_array[0:,5]=='yes'
cellular = banking_array[0:,6]=='cellular'
cond = (personal_loan & cellular)
print(np.count_nonzero(cond))