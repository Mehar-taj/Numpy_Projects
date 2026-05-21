#Find the count who are single but have more than avg bank balance
import numpy as np
from Bank_dataset import banking_array
singles = banking_array[0:,2]=='single'
avg_bank_balancle = banking_array[0:,3]
cond = (singles & (avg_bank_balancle > avg_bank_balancle.mean()))
print(cond)
print(np.count_nonzero(cond))