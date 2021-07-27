#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('writefile', 'D:\\pywork\\my_area.py', '    \nPI = 3.14\n\ndef square_area(a):\n    return a ** 2 # 정사각형 넓이\n\ndef circle_area(r):\n    return PI * r ** 2 # 원의 넓이')


# In[2]:


cd D:\pywork


# In[3]:


import my_area # 모듈 불러오기

print('pi =', my_area.PI) # 모듈의 변수 이용
print('square area =', my_area.square_area(5)) # 모듈의 함수 이용
print('circle area =', my_area.circle_area(2))


# In[4]:


from my_area import PI, square_area, circle_area

print('pi =', PI) # 모듈의 변수 이용
print('square area =', square_area(5)) # 모듈의 함수 이용
print('circle area =', circle_area(2))


# In[5]:


import my_area as ma # 모듈명에 별명을 붙임

print('pi =', ma.PI) # 모듈명 대신 별명 이용
print('square area =', ma.square_area(5))
print('circle area =', ma.circle_area(2))


# In[6]:


from my_area import PI as pi
from my_area import square_area as square
from my_area import circle_area as circle

print('pi =', PI) # 모듈 변수의 별명 이용
print('square area =', square_area(5)) # 모듈 함수의 별명 이용
print('circle area =', circle_area(2))


# In[7]:


mkdir D:\pywork\image; D:\pywork\image\io_file


# In[8]:


get_ipython().run_cell_magic('writefile', 'D:\\pywork\\image\\__init__.py', '# File name: __init__.py')


# In[9]:


get_ipython().run_cell_magic('writefile', 'D:\\pywork\\image\\io_file\\__init__.py', '# File name: __init__.py')


# In[10]:


get_ipython().run_cell_magic('writefile', 'D:\\pywork\\image\\io_file\\imgread.py', '# File name: imgread.py\n\ndef pngread():\n    print("pngread in imgread module")\n\ndef jpgread():\n    print("jpgread in imgread module")')


# In[11]:


get_ipython().system('tree /F')


# In[12]:


import image.io_file.imgread

image.io_file.imgread.pngread()
image.io_file.imgread.jpgread()


# In[13]:


from image.io_file import imgread
imgread.pngread()
imgread.jpgread()


# In[14]:


from image.io_file.imgread import pngread, jpgread

pngread()
jpgread()


# In[15]:


from image.io_file import imgread as img

img.pngread()
img.jpgread()


# In[ ]:




