''' 
Company has decided if the age if the customer is less than 45 his balance will be credited with 2000
and if it is above the credit 1000
'''
import numpy as np
from Bank_dataset import banking_array
age_ls_45 = banking_array[0:,0]
age_gt_45 = banking_array[0:,0]
bank_balance = banking_array[0:,3]
cond1 = age_gt_45 > 45
credit_amt1 = bank_balance[cond1]+1000
print(bank_balance[cond1])
print(credit_amt1)
cond2 = age_ls_45 < 45
credit_amt2 = bank_balance[cond2]+2000
print(bank_balance[cond2])
print(credit_amt2)