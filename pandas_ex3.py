#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('writefile', 'D:\\pywork\\sea_rain1.csv', '연도,동해,남해,서해,전체\n1996, 17.4629, 17.2288, 14.436, 15.9067\n1997, 17.4116, 17.4092, 14.8248, 16.1526\n1998, 17.5944, 18.011, 15.2512, 16.6044\n1999, 18.1495, 18.3175, 14.8979, 16.6284\n2000, 17.9288, 18.1766, 15.0504, 16.6178')


# In[2]:


import pandas as pd

pd.read_csv('D:/pywork/sea_rain1.csv')


# In[3]:


get_ipython().run_cell_magic('writefile', 'D:\\pywork\\sea_rain1_space.txt', '연도,동해,남해,서해,전체\n1996, 17.4629, 17.2288, 14.436, 15.9067\n1997, 17.4116, 17.4092, 14.8248, 16.1526\n1998, 17.5944, 18.011, 15.2512, 16.6044\n1999, 18.1495, 18.3175, 14.8979, 16.6284\n2000, 17.9288, 18.1766, 15.0504, 16.6178')


# In[6]:


pd.read_csv('D:/pywork/sea_rain1_space.txt', sep=" ")


# In[7]:


pd.read_csv('D:/pywork/sea_rain1.csv', index_col = "연도")


# In[8]:


df_WH = pd.DataFrame({'Weight':[62, 67, 55, 74],
                      'Height':[165, 177, 160, 180]},
                       index=['ID_1', 'ID_2', 'ID_3', 'ID_4'])
df_WH.index.name ='User'
df_WH


# In[9]:


bmi = df_WH['Weight']/(df_WH['Height']/100)**2
bmi


# In[10]:


df_WH['BMI'] = bmi
df_WH


# In[11]:


df_WH.to_csv('D:/pywork/save_DataFrame.csv')


# In[ ]:




