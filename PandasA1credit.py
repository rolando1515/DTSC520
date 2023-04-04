#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


Q1 = pd.Series(['Stina Calista', 'Fran Hendrix', 'Cyril Isak', 'Danilo Norina'],
               index=[5281224, 4223241, 4233342, 5012332])


# In[ ]:


Q2 = {'Roger Clemens': 133.7, 'Cy Young': 131.5, 'Walter Johnson': 117.1,
      'Greg Maddux': 116.7, 'Randy Johnson': 110.4}


# In[ ]:


Q3 = pd.Series(Q2)


# In[ ]:


occupation = pd.Series(['Accountant', 'Data scientist', 'Manager', 'Security staff'],
                       index=[5281224, 4223241, 4233342, 5012332])


# In[ ]:


Q4 = pd.DataFrame({'Name': Q1, 'Occupation': occupation})


# In[ ]:


pop_dict = {'China': 1411778724, 'India': 1378331486, 'United States': 331865271,
            'Indonesia': 271350000, 'Pakistan': 225200000}


# In[ ]:


area_dict = {'Russia': 17098246, 'Canada': 9984670, 'China': 9596961,
             'United States': 9525067, 'Brazil': 8515767}


# In[ ]:


Q5 = pd.DataFrame({'Population': pop_dict, 'Area': area_dict})


# In[ ]:


Q6 = Q5.loc[['China', 'United States']]


# In[ ]:


Q7 = Q5.loc[Q5['Population'] > 270000000]


# In[ ]:


Q8 = Q5.loc[Q5['Area'] > 9600000]

