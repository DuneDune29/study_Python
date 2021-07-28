#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


s1 = pd.Series([10, 20, 30, 40, 50])
s1


# In[4]:


s1.index
print(s1.index)


# In[5]:


s1.values


# In[6]:


s2 = pd.Series(['a', 'b', 'c', 1, 2, 3])
s2


# In[7]:


import numpy as np

s3 = pd.Series([np.nan, 10, 30])
s3


# In[8]:


index_date = ['2018-10-07', '2018-10-08', '2018-10-09', '2018-10-10']
s4 = pd.Series([200, 195, np.nan, 205], index = index_date)
s4


# In[9]:


s5 = pd.Series({'국어': 100, '영어': 95, '수학': 90})
s5


# In[10]:


pd.date_range(start = '2019-01-01', end = '2019-01-07')


# In[11]:


index_date = pd.date_range(start = '2021-02-01', periods = 5, freq = 'D')
pd.Series([51, 62, 55, 49, 58], index = index_date)


# In[13]:


pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


# In[14]:


data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
index_date = pd.date_range('2019-09-01', periods = 4)
columns_list = ['A', 'B', 'C']
pd.DataFrame(data, index = index_date, columns = columns_list)


# In[16]:


table_data = {'연도': [2015, 2016, 2016, 2017, 2017],
              '지사': ['한국', '한국', '미국', '한국', '미국'],
              '고객 수': [200, 250, 450, 300, 500]}
table_data


# In[17]:


pd.DataFrame(table_data)


# In[18]:


df = pd.DataFrame(table_data, columns=['연도', '지사', '고객 수'])
df


# In[19]:


df.index


# In[20]:


df.columns


# In[21]:


df.values


# In[ ]:




