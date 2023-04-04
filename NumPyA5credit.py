#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[ ]:


np.random.seed(5)


# In[ ]:


ar = np.random.randint(0, 15, size = 20)


# In[ ]:


Q1 = ar[3]


# In[ ]:


Q2 =ar[8:]


# In[ ]:


Q3 = ar[1:19:2]


# In[ ]:


np.random.seed(6)


# In[ ]:


ar1 = np.random.randint(0,15, size=(7, 8))


# In[ ]:


Q4 = ar1[4, 5]


# In[ ]:


Q5 = ar1[0:2, 5:8]


# In[ ]:


np.random.seed(10)


# In[ ]:


Q6 = np.random.randint(0,15, size=(4, 5))


# In[ ]:


Q6[2, 2] = 4


# In[ ]:


Q7 = Q6[1:, :3]


# In[ ]:


np.random.seed(8)


# In[ ]:


Q8 = np.random.randint(0,15, size=(4, 5))


# In[ ]:


Q9 = Q8[1:, :3].copy()


# In[ ]:


Q9[1, 2] = 4


# In[ ]:


np.random.seed(20)


# In[ ]:


ar2 = np.random.randint(0,15, size=(2, 6))


# In[ ]:


Q10 = ar2.reshape((4, 3))


# In[ ]:


np.random.seed(15)


# In[ ]:


ar3 = np.random.randint(0,15, size=10)


# In[ ]:


Q11 = ar3.reshape((10, 1))


# In[ ]:


np.random.seed(9)


# In[ ]:


ar4 = np.random.randint(0,15, size=(5,3))


# In[ ]:


Q12 = ar4[3].copy()

