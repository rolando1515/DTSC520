#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[ ]:


q1 = {'One': 'A', 'Two': 'B', 'Three': 'C', 'Four': 'D'}


# In[ ]:


Q1 = q1['Three']


# In[ ]:


Q2 = {'Five': 'E', 'Six': 'F'}


# In[ ]:


Q2['Seven'] = 'G'


# In[ ]:


Q3 = {'Eight': 'H'}


# In[ ]:


del Q3['Eight']


# In[ ]:


Q4 = {'Nine': 'I', 'Ten': 'J'}


# In[ ]:


Q4['Ten'] = 'K'


# In[ ]:


def Q5():
    for Q5 in q1.values():
        print(Q5)


# In[ ]:


def Q6():
    for Q6 in q1.keys():
        print(Q6)


# In[ ]:


Q7 = Q7 = {'Least Favorite': {'Fruit': 'Grape', 'Color': 'Purple'},
          'Medium Favorite': {'Fruit': 'Apple', 'Color': 'Red'},
          'Most Favorite': {'Fruit': 'Banana', 'Color': 'Yellow'}
          }

