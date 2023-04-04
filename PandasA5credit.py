import numpy as np
import pandas as pd

np.random.seed(12)

# Q1
index = pd.MultiIndex.from_product([['one', 'two', 'three'], [1, 2]])
Q1 = pd.Series([11, 111, 22, 222, 33, 333], index=index)

# Q2
Q2 = Q1.loc[('one', 1):('three', 2)]

# Q3
Q3 = Q1.unstack().loc[['One', 'Two', 'Three']].stack()

# Q4
Q4 = pd.Series([11, 111, 22, 222, 33, 333], index=index).unstack()

# Q5
Q5 = Q4.sum()

# Q6
Q6 = pd.DataFrame(np.random.randint(0, 9, size=(3, 2)), columns=['A', 'B'], index=[('1', 'a'), ('1', 'b'), ('2', 'a')])

# Q7
index = pd.MultiIndex.from_product([['ONE', 'TWO', 'THREE'], ['one', 'two']])
columns = pd.MultiIndex.from_product([['A', 'B'], ['a', 'b', 'c', 'd']])
Q7 = pd.DataFrame(np.random.randint(0, 20, size=(6, 8)), index=index, columns=columns)

# Q8
s1 = pd.Series([7, 8, 9, 10], index=['ONE', 'TWO', 'THREE', 'FOUR'])
s2 = pd.Series([11, 12, 13, 14], index=['ONE', 'FOUR', 'FIVE', 'SIX'])
Q9 = pd.concat([s1, s2], axis=1)

# Q10
Q10 = pd.concat([s1, s2])

# Q11
s3 = pd.Series([7, 8, 9, 10], name='A', index=['ONE', 'TWO', 'THREE', 'FOUR'])
s4 = pd.Series([11, 12, 13, 14], name='B', index=['THREE', 'FOUR', 'FIVE', 'SIX'])
Q11 = pd.concat([s3, s4], axis=1)

# Q12
s5 = pd.Series([15, 16], index=['SEVEN', 'EIGHT'])
df1 = pd.concat([s1, s2], axis=1)
df2 = pd.concat([s3, s4, s5], axis=1)
Q12 = pd.concat([df1, df2], axis=0)

print(Q1)