#!/usr/bin/env python
# coding: utf-8

# In[1]:


cd d:\pywork


# In[2]:


f = open('myFile.txt', 'w')
f.write('This is my first file.')
f.close()


# In[3]:


f = open('myFile.txt', 'r')
file_text = f.read()
f.close()

print(file_text)


# In[4]:


f = open('two_times_table.txt', 'w')
for num in range(1, 6):
    format_string = "2 x {0} = {1}\n".format(num, 2*num)
    f.write(format_string)
f.close()


# In[5]:


f = open("two_times_table.txt")
line = f.readline()
while line:
    print(line, end = "")
    line = f.readline()
f.close()


# In[6]:


f = open("two_times_table.txt")
lines = f.readlines()
f.close()

print(lines)


# In[7]:


f = open("two_times_table.txt")
lines = f.readlines()
f.close()
for line in lines:
    print(line, end="")


# In[8]:


f = open("two_times_table.txt")
for line in f:
    print(line, end="")
f.close()


# In[9]:


with open('myTextFile3.txt', 'w') as f:
    for num in range(1, 6):
        format_str = "3 x {0} = {1}\n".format(num, 3*num)
        f.write(format_str)


# In[10]:


with open('myTextFile3.txt', 'r') as f:
    for line in f:
        print(line, end="")


# In[ ]:




