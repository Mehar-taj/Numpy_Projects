#Find the count of customers whose age is greater than 35 and less than 50 and also find the bank balance of these customers
import numpy as np
from Bank_dataset import banking_array
age_gt_35 = banking_array[0:,0]>35
age_ls_50 = banking_array[0:,0]<50
bank_balance = banking_array[0:,3]
cond = (age_gt_35 & age_ls_50)
print("the count of customers whose age is greater than 35 and less than 50",np.count_nonzero)
print('accessing bank_balance of coustomers whose age is greater than 35 and less than 50',bank_balance[cond])
#total balace of this customers
print('Total balance of this customers',bank_balance[cond].sum())
