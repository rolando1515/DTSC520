#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[ ]:


q1 = np.array([2, 4, 6, 8, 10, 12, 14, 16])


# In[ ]:


Q1 = [q1[6], q1[2], q1[5]]


# In[ ]:


q2 = q1[[1, 3, 2, 0, 7, 4]]


# In[ ]:


Q2 = q2.reshape((2, 3))


# In[ ]:


Q3 = q1.reshape((4, 2))


# In[ ]:


q4 = Q3[0,0:2]


# In[ ]:


Q4 =q4[[1, 0]]


# In[ ]:


Q5 = Q3[0:2, 0:1]


# In[ ]:


np.random.seed(6)


# In[ ]:


Q6 = np.random.randint(0, 10, size=10)


# In[ ]:


Q6.sort()


# In[ ]:


q7 = np.random.randint(0, 10, size=(4, 5))


# In[ ]:


Q7 = np.sort(q7, axis=0)


# In[ ]:


Q8 = np.sort(q7, axis=1)


# In[ ]:


q9 = np.array([('Grape', 'Purple', 3), 
               ('Apple', 'Red', 2), 
               ('Banana', 'Yellow', 1)], 
              dtype=[('Fruit', 'U10'), ('Color', 'U10'), ('Ranking', int)])


# In[ ]:


Q9 = q9['Color']


# In[ ]:


Q10 = q9[2]


# In[ ]:


Q11 = q9[q9['Ranking'] < 3]

