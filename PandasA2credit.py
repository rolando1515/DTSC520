#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


odd_numbers = pd.Series(range(3, 12, 2))


# In[ ]:


Q1 = odd_numbers.values


# In[ ]:


Q2 = odd_numbers.index


# In[ ]:


Q3 = odd_numbers[2]


# In[ ]:


Q4 = odd_numbers[[2, 3]]


# In[ ]:


Q5 = pd.Series([3, 5, 7, 9, 11], index=['three', 'five', 'seven', 'nine', 'eleven'])


# In[ ]:


di = {'Da': 'ta', 'Sc': 'ie', 'nc': 'ef', 'or': 'all'}


# In[ ]:


Q6 = pd.Series(di)


# In[ ]:


Q7 = Q6['nc']


# In[ ]:


Q8 = Q6[['Sc', 'nc', 'or']]


# In[ ]:


s1 = pd.Series({'A': 'a', 'B': 'b', 'C': 'c'}, name='Lowercase')
s2 = pd.Series({'A': 1, 'B': 2, 'C': 3}, name='numbers')
Q9 = pd.concat([s1, s2], axis=1)


# In[ ]:


Q10 = Q9.index


# In[ ]:


Q11 = Q9.columns


# In[ ]:


Q12 = Q9['numbers']

