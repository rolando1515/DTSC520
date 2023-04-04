#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[ ]:


Q1 = np.zeros(20, dtype = float)


# In[ ]:


Q2 = np.ones((4,5), dtype=int)


# In[ ]:


Q3 = np.full((2,5), 2, dtype = float)


# In[ ]:


Q4 = np.arange(0, 50, dtype = float)


# In[ ]:


Q5 = np.linspace(4, 18, 9)


# In[ ]:


Q6 = np.zeros((5, 5), dtype=int)


# In[ ]:


np.fill_diagonal(Q6, 1)


# In[ ]:


np.random.seed(10)


# In[ ]:


Q7 = np.random.rand(4, 2) 


# In[ ]:


np.random.seed(9)


# In[ ]:


Q8 = np.random.randint(0, 16, size = (4, 2, 5))


# In[ ]:


Q9 = np.size(Q8)

