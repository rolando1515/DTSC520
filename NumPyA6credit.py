#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[ ]:


np.random.seed(100)


# In[ ]:


ar = np.random.rand(20)


# In[ ]:


Q1 = np.sum(ar)


# In[ ]:


Q2 = np.max(ar)


# In[ ]:


arr2 = np.random.rand(4, 5)


# In[ ]:


Q3 = np.min(arr2, axis=1)


# In[ ]:


Q4 = np.mean(arr2)


# In[ ]:


ar2 = np.array([2, 3, np.nan, 5])


# In[ ]:


Q5 = np.nansum(ar2)


# In[ ]:


ar3 = np.random.rand(4)


# In[ ]:


ar4 = np.random.rand(4)


# In[ ]:


Q6 = np.concatenate((ar3, ar4))


# In[ ]:


q7 = np.random.rand(4, 4)


# In[ ]:


Q7 = np.concatenate((q7, q7))


# In[ ]:


q8 = np.random.rand(2, 4)


# In[ ]:


Q8 = np.vstack((q7, q8))


# In[ ]:


Q9 = np.vstack((q7, q7, q7, q8, q8))


# In[ ]:


ar5 = np.random.rand(2, 1)


# In[ ]:


Q10 = np.hstack((q8, ar5))


# In[ ]:


q11 = np.random.rand(20)


# In[ ]:


Q11a, Q11b = np.split(q11, [5])


# In[ ]:


Q12a, Q12b, Q12c = np.split(q11, [10, 15])


# In[ ]:


q13 = np.random.rand(5, 5)


# In[ ]:


Q13a, Q13b = np.vsplit(q13, [3])


# In[ ]:


Q14a, Q14b = np.hsplit(q13, [3])

