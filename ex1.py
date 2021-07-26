#!/usr/bin/env python
# coding: utf-8

# In[1]:


1+2


# In[3]:


a = 30
b = 40
print(a <= b)


# In[4]:


17


# In[ ]:





# In[6]:


0b10001


# In[8]:


0o21


# In[9]:


0x11


# In[11]:


bin(17)


# In[13]:


oct(17)


# In[15]:


hex(17)


# In[17]:


type(True)


# In[19]:


print(True and False)


# In[21]:


print(not True)


# In[23]:


print(5 != 3)


# In[25]:


print(5 == 3)


# In[27]:


5 * 3


# In[29]:


5 / 3


# In[31]:


5 // 3


# In[33]:


5 % 3


# In[36]:


5 ** 3


# In[38]:


abc = 1234
print(abc * 1 / 2)


# In[40]:


string1 = 'Hello'
string2 = "Hello"
type(string1)


# In[42]:


print(type(string1))


# In[44]:


print(type(3))


# In[46]:


str3 = 'This is "test1"'
str4 = "This is 'test2'"
print(str3, str4)


# In[47]:


str5 = '''삼중 작은 따옴표
여러줄 처리
에 사용'''


# In[48]:


str6 = """삼중 큰 따옴표
여러줄 처리
에 사용"""


# In[50]:


print(str5)
print(str6)


# In[52]:


print(string1)
print(string2)


# In[54]:


print(string1, string2)


# In[56]:


x = 10
y = 20
print('x = ' + x + ', y = ' + y)


# In[58]:


print('x = ' + str(x) + ', y = ' + str(y))


# In[60]:


score1 = 80
score2 = 87
sum = score1 + score2
avg = sum / 2

print('두 과목 점수 : %d, %d' % (score1, score2))
print('합계 : %d, 평균 : %.2f' % (sum, avg))


# In[65]:


year = 2021
month = 2
day = 16
print(year, month, day, sep='-')


# In[66]:


a = '안녕'
b = '반가워'
print(a)
print(b)
print('\n\n')
print(a, end=' ')
print(b)


# In[68]:


st = 'Python String Test'
print(st)


# In[70]:


print(st[3:7]) # 문자열 슬라이싱


# In[72]:


print(st[3:])


# In[74]:


print(st[:9])


# In[76]:


print(st[:])


# In[9]:


a = input('숫자 입력:')
b = input('또 숫자 입력:')
c = a + b
print(c)


# In[13]:


student1 = [90, 95, 85, 80]
student1


# In[15]:


type(student1)


# In[17]:


print(type(student1))


# In[19]:


student1[0]


# In[21]:


student1[-1]


# In[27]:


student1[1] = 100
student1


# In[29]:


myFriends = ['James', 'Robert', 'Lisa', 'Mary']
myFriends


# In[32]:


myFriends[-2] = 'Elsa'
myFriends


# In[34]:


mixedList = [0, 2, 3.14, 'python', 'program', True, myFriends]
mixedList


# In[36]:


list_con1 = [1, 2, 3, 4]
list_con2 = [5, 6, 7, 8]
list_con = list_con1 + list_con2 # 리스트 연결

print(list_con)


# In[38]:


list_con = list_con1 * 3 # 리스트 반복
print(list_con)


# In[39]:


st = "Python" * 3
print(st)

