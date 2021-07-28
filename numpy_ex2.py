#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[4]:


arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])


# In[5]:


arr1 + arr2


# In[6]:


arr1 * arr2


# In[7]:


arr1 / (arr2 ** 2)


# In[8]:


arr1 > 20


# In[9]:


arr3 = np.arange(5)
arr3


# In[10]:


[arr3.sum(), arr3.mean()]


# In[11]:


[arr3.std(), arr3.var()]


# In[12]:


arr4 = np.arange(1, 5)
arr4


# In[13]:


arr4.cumsum()


# In[14]:


arr4.cumprod()


# In[16]:


a1 = np.array([0, 10, 20, 30, 40, 50])
a1


# In[17]:


a1[0]


# In[18]:


a1[[1,3,4]]


# In[19]:


a2 = np.arange(10, 100, 10).reshape(3, 3)
a2


# In[20]:


a2[0, 2]


# In[22]:


a2[2, 2] = 95
a2


# In[23]:


a2[1]


# In[25]:


a2[1] = [47, 57, 67]
a2


# In[26]:


a2[[0, 2], [0, 1]]


# In[27]:


a = np.array([1, 2, 3, 4, 5, 6])
a[a > 3]


# In[28]:


a[(a % 2) == 0]


# In[29]:


b1 = np.array([0, 10, 20, 30, 40, 50])
b1[1:4]


# In[30]:


b1[2:5] = np.array([25, 35, 45])
b1


# In[31]:


b1[3:6] = 60
b1


# In[34]:


b2 = np.arange(10, 100, 10).reshape(3, 3)
b2


# In[35]:


b2[1:3, 1:3]


# In[36]:


b2[1][0:2]


# In[37]:


b2[0:2, 1:3] = np.array([[25, 35], [55, 65]])
b2


# In[ ]:




