'''
Company has decided to give a bonus of 5% of their account balance to those account holder where age is more than or equal
to 55 yrs and whose account balance is more than 2000. Calculate the sum of the total bank balance to the account holders after
creadting their bonus account.
'''
import numpy as np
from Bank_dataset import banking_array
age_gt_55 = banking_array[0:,0]
bank_balance = banking_array[0:,3]
cond1 = (age_gt_55 >= 55)
cond2 = (bank_balance > 2000)
cond = (cond1 & cond2)
print(cond)
tol_bal = bank_balance[cond]
print(tol_bal)
bonus = tol_bal*0.05
aft_bonus = tol_bal+bonus
print(aft_bonus)