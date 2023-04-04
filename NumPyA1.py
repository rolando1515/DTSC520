#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[ ]:


Q1 = [2, 8, 7, 11]


# In[ ]:


Q1 = np.array(Q1)


# In[ ]:


Q2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


# In[ ]:


Q3 = Q2[[0, 1, 2], [1, 1, 1]][:, np.newaxis]


# In[ ]:


np.random.seed(6)


# In[ ]:


Q4 = np.random.randint(0,10, size = (5,6))


# In[ ]:


Q5 = Q4[[0, 1, 2], 1:3]


# In[ ]:


Q6 = Q4[[3, 4], 2:5]


# In[ ]:


Q7 = Q4[2:4, 1:3]


# In[ ]:


Q8 = Q4[:, 2:4]


# In[ ]:


Q9 = Q4[3:, :6]

