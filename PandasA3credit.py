import numpy as np
import pandas as pd

# Q1
Q1 = np.array([2, np.nan, 6, 7, 3, 2])

# Q2
Q2 = np.sum(Q1)

# Q3
Q3 = pd.Series([4.0, 5.0, 2.0, np.nan, 1.0, np.nan])

# Q4
Q4 = Q3.isnull()

# Q5
Q5 = pd.Series([4.0, 5.0, 2.0, np.nan, 1.0, np.nan])
Q5 = Q5[Q5.notnull()]

# Q6
Q6 = pd.Series([4.0, 5.0, 2.0, np.nan, 1.0, np.nan])
Q6 = Q6.fillna(100)

# Q7
Q7 = pd.DataFrame([[4, 5.0, 2.0, 9.0, 1.0, 8],
                   [5, 6.0, np.nan, 3.0, np.nan, 2],
                   [6, np.nan, 7.0, np.nan, 4.0, 3]])

Q7 = Q7.fillna(100)

# Q8
Q8 = pd.Series([4.0, 5.0, 2.0, np.nan, 1.0, np.nan])
Q8 = Q8.dropna()

# Q9
Q9 = pd.DataFrame([[4, 5.0, 2.0, 9.0, 1.0, 8],
                   [5, 6.0, np.nan, 3.0, np.nan, 2],
                   [6, np.nan, 7.0, np.nan, 4.0, 3]])

Q9 = Q9.dropna(axis=1)

# Q10
Q10 = pd.DataFrame([[4, 5.0, 2.0, 9.0, 1.0, 8],
                    [5, 6.0, np.nan, 3.0, np.nan, 2],
                    [6, np.nan, 7.0, np.nan, 4.0, 3]])

Q10 = Q10.dropna()

# Q11
Q11 = pd.DataFrame([[4, 5.0, 2.0, 9.0, 1.0, 8],
                    [5, 6.0, np.nan, 3.0, np.nan, 2],
                    [6, np.nan, 7.0, np.nan, 4.0, 3]])

Q11 = Q11.dropna(thresh=5)

# Q12
Q12 = pd.DataFrame([[4, 5.0, 2.0, 9.0, 1.0, 8],
                    [5, 6.0, np.nan, 3.0, np.nan, 2],
                    [6, np.nan, 7.0, np.nan, 4.0, 3]])

Q12[6] = np.nan

print(5)