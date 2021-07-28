#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([10, 20, 30, 40, 50])
s1 + s2


# In[3]:


s2 / s1


# In[4]:


s3 = pd.Series([1, 2, 3, 4])
s4 = pd.Series([10, 20 , 30, 40, 50])
s3 + s4


# In[5]:


table_data1 = {'A': [1, 2, 3, 4, 5],
              'B': [10, 20, 30, 40, 50],
              'C': [100, 200, 300, 400, 500]}
df1 = pd.DataFrame(table_data1)
df1


# In[7]:


table_data2 = {'A': [6, 7, 8],
              'B': [60, 70, 80],
              'C': [600, 700, 800]}
df2 = pd.DataFrame(table_data2)
df2


# In[8]:


df1 + df2


# In[9]:


table_data3 = {'봄': [256.5, 264.3, 215.9, 223.2, 312.8],
              '여름': [770.6, 567.5, 599.8, 387.1, 446.2],
              '가을': [363.5, 231.2, 293.1, 247.7, 381.6],
              '겨울': [139.3, 59.9, 76.9, 109.1, 108.1]}
columns_list = ['봄', '여름', '가을', '겨울']
index_list = ['2012', '2013', '2014', '2015', '2016']

df3 = pd.DataFrame(table_data3, columns = columns_list, index = index_list)
df3


# In[10]:


df3.mean()


# In[11]:


df3.mean(axis = 1)


# In[12]:


df3.describe()


# In[13]:


KTX_data = {'경부선 KTX': [39060, 39896, 42005, 43621, 41702, 41266, 32427],
            '호남선 KTX': [7313, 6967, 6873, 6626, 8675, 10622, 9228],
            '경전선 KTX': [3627, 4168, 4088, 4424, 4606, 4984, 5570],
            '전라선 KTX': [309, 1771, 1954, 2244, 3146, 3945, 5766],
            '동해선 KTX': [np.nan, np.nan, np.nan, np.nan, 2395, 3786, 6667]}
col_list = ['경부선 KTX','호남선 KTX', '경전선 KTX', '전라선 KTX', '동해선 KTX']
index_list = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']

df_KTX = pd.DataFrame(KTX_data, columns = col_list, index = index_list)
df_KTX


# In[15]:


df_KTX.head()


# In[16]:


df_KTX.tail()


# In[17]:


df_KTX.head(3)


# In[18]:


df_KTX.tail(2)


# In[19]:


df_KTX[1:2]


# In[20]:


df_KTX[2:5]


# In[21]:


df_KTX.loc['2011']


# In[22]:


df_KTX.loc['2013':'2016']


# In[23]:


df_KTX['경부선 KTX']


# In[24]:


df_KTX['경부선 KTX']['2012':'2014']


# In[25]:


df_KTX['경부선 KTX'][2:5]


# In[26]:


df_KTX.loc['2016']['호남선 KTX']


# In[27]:


df_KTX.loc['2016', '호남선 KTX']


# In[28]:


df_KTX['호남선 KTX']['2016']


# In[29]:


df_KTX['호남선 KTX'][5]


# In[30]:


df_KTX['호남선 KTX'].loc['2016']


# In[31]:


df_KTX


# In[32]:


df_KTX.T


# In[33]:


df_KTX[['동해선 KTX', '전라선 KTX', '경부선 KTX']]


# In[34]:


df1 = pd.DataFrame({'Class1' : [95, 92, 98, 100],
                    'Class2' : [91, 93, 97, 99]})
df1


# In[35]:


df2 = pd.DataFrame({'Class1' : [87, 89],
                    'Class2' : [85, 90]})
df2


# In[36]:


df1.append(df2)


# In[37]:


df1.append(df2, ignore_index=True)


# In[38]:


df3 = pd.DataFrame({'Class1' : [96, 83]})
df3


# In[39]:


df2.append(df3, ignore_index=True)


# In[40]:


df4 = pd.DataFrame({'Class3' : [93, 91, 95, 98]})
df4


# In[41]:


df1.join(df4)


# In[42]:


index_label = ['a', 'b', 'c', 'd']
df1a = pd.DataFrame({'Class1': [95, 92, 98, 100],
                    'Class2': [91, 93, 97, 99]}, index = index_label)
df4a = pd.DataFrame({'Class3': [93, 91, 95, 98]}, index = index_label)

df1a.join(df4a)


# In[43]:


df5 = pd.DataFrame({'Class4': [82, 92]})
df5


# In[44]:


df1.join(df5)


# In[45]:


df_A_B = pd.DataFrame({'판매월': ['1월', '2월', '3월', '4월'],
                       '제품A': [100, 150, 200, 130],
                       '제품B': [90, 110, 140, 170]})
df_A_B


# In[46]:


df_C_D = pd.DataFrame({'판매월': ['1월', '2월', '3월', '4월'],
                       '제품C': [112, 141, 203, 134],
                       '제품D': [90, 110, 140, 170]})
df_C_D


# In[47]:


df_A_B.merge(df_C_D)


# In[48]:


df_left = pd.DataFrame({'key': ['A', 'B', 'C'], 'left': [1, 2, 3]})
df_left


# In[49]:


df_right = pd.DataFrame({'key': ['A', 'B', 'D'], 'right': [4, 5, 6]})
df_right


# In[50]:


df_left.merge(df_right, how = 'left', on = 'key')


# In[51]:


df_left.merge(df_right, how = 'right', on = 'key')


# In[52]:


df_left.merge(df_right, how = 'outer', on = 'key')


# In[53]:


df_left.merge(df_right, how = 'inner', on = 'key')


# In[ ]:




