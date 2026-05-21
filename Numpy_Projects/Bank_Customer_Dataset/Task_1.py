#Finding unique values from the employment column
import numpy as np
from Bank_dataset import banking_array
print(np.unique(banking_array[0:,1]))