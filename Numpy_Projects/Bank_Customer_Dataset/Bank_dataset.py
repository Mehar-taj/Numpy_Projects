import numpy as np
# Dataset → [Age , Employment , Marital Status , Balance , Personal Loan , Car Loan , Connection , Month]
banking_array = np.array([
    [33.0, 'services',     'married',    1787.0, 'no',  'no', 'cellular', 'oct'],
    [35.0, 'management',   'single',     4789.0, 'yes', 'yes','cellular','may'],
    [30.0, 'management',   'married',    1350.0, 'yes', 'no', 'cellular','apr'],
    [59.0, 'management',   'married',    1476.0, 'yes','yes','unknown','jun'],
    [59.0, 'blue-collar',  'married',    0.0,    'no',  'no', 'unknown','may'],
    [36.0, 'management',   'single',     747.0,  'no',  'no', 'cellular','feb'],
    [36.0, 'self-employed','married',     307.0, 'yes','no','cellular','may'],
    [39.0, 'technician',   'married',     147.0, 'no', 'no','cellular','may'],
    [41.0, 'entrepreneur', 'married',     221.0, 'yes','no','unknown','may'],
    [43.0, 'services',     'married',    -88.0, 'yes','yes','cellular','apr'],
    [39.0, 'services',     'married',     132.0, 'no', 'no','cellular','jul'],
    [59.0, 'management',   'married',    40000, 'yes','yes','unknown','jun'],
    [59.0, 'blue-collar',  'married',   5000,    'no',  'no', 'unknown','may'],
], dtype=object)