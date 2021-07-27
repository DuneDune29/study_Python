#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


data1 = [0, 1, 2, 3, 4, 5]
a1 = np.array(data1)
a1


# In[3]:


data2 = [0.1, 5, 4, 12, 0.5]
a2 = np.array(data2)
a2


# In[4]:


a1.dtype


# In[5]:


a2.dtype


# In[6]:


np.array([0.5, 2, 0.01, 8])


# In[7]:


np.array(([1,2,3], [4,5,6], [7,8,9]))


# In[8]:


np.arange(0, 10, 2)


# In[9]:


np.arange(1, 10)


# In[10]:


np.arange(5)


# In[11]:


np.arange(12).reshape(4,3)


# In[12]:


b1 = np.arange(12).reshape(4,3)
b1.shape


# In[13]:


b2 = np.arange(5)
b2.shape


# In[15]:


t1 = (1)
t1


# In[16]:


t2 = (1,)
t2


# In[17]:


np.linspace(1, 10, 10)


# In[18]:


np.linspace(0, np.pi, 20)


# In[19]:


np.zeros(10)


# In[20]:


np.zeros((3,4))


# In[22]:


np.eye(3) # 단위 행렬(특수 배열)


# In[23]:


np.array(['1.5', '0.62', '2', '3.14', '3.141592'])


# In[24]:


str_a1 = np.array(['1.567', '0.123', '5.123', '9', '8'])
num_a1 = str_a1.astype(float)
num_a1


# In[25]:


str_a1.dtype


# In[26]:


num_a1.dtype


# In[ ]:




