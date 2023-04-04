#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[ ]:


np.random.seed(56)


# In[ ]:


Q1 = np.random.randint(0, 20, size = (10, 10))


# In[ ]:


Q2 = Q1[2:5, 3:8]


# In[ ]:


Q3 = Q1[7:, 4:6]


# In[ ]:


Q4 = Q3.reshape(2, 3)


# In[ ]:


x = np.random.randint(0, 15, size = 10)
y = np.random.randint(0, 15, size = 10)
Q5 = np.concatenate([x, y])


# In[ ]:


Q6a, Q6b, Q6c, Q6d = np.split(Q5, [4, 11, 17])


# In[ ]:


Q7 = np.sum(Q5)


# In[ ]:


Q8 = np.mean(np.random.randint(48, 86, size=50))


# In[ ]:


Q9_data = [('Jonathan Loaisiga', 'Baseball player', 595800.00),
           ('Nick Saban', 'Football coach', 8619934.23),
           ('Katie Ladecky', 'Swimmer', 100000.00)]


# In[ ]:


Q9 = np.array(Q9_data, dtype=[('Name', 'U20'), ('Occupation', 'U20'), ('Salary', 'f8')])

