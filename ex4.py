#!/usr/bin/env python
# coding: utf-8

# In[7]:


animal_0 = "cat"
animal_1 = "dog"
animal_2 = "fox"

print("Animal: {0}".format(animal_0))
print("Animal: {0}, {1}, {2}".format(animal_0, animal_1, animal_2))


# In[9]:


print("Animal: {1}, {2}, {0}".format(animal_0, animal_1, animal_2))
print("Animal: {0}, {2}".format(animal_0, animal_1, animal_2))
print("Animal: {}, {}, {}".format(animal_0, animal_1, animal_2))


# In[11]:


a = 0.123456789
print("{0:.2f}, {0:.5f}".format(a))


# In[15]:


x = 85
if x >= 90:
        print("Pass")
print('end')


# In[18]:


x = int(input('숫자를 입력하세요 :'))
if x > 0 :
    print('양수!')
else :
    print('0 또는 음수!')


# In[21]:


num = int(input('숫자를 입력하세요 :'))
if num % 2 == 0 :
    print('짝수이다.')
else :
    print('홀수이다.')


# In[23]:


id = input('아이디를 입력하세요 :')
level = int(input('회원 레벨을 입력하세요 : '))
if id == 'admin' or level == 1 :
    print('관리자이다.')
else :
    print('관리자가 아니다.')


# In[25]:


name = input('이름을 입력하세요 : ')
if not name :
    print('이름이 입력되지 않았다')
else :
    print('이름 : %s' % name)


# In[27]:


x = int(input('점수 입력 :'))
if x >= 90:
    print("Very good")
elif (x >= 80) and (x <90):
    print("Good")
else :
    print("Bad")
print('성적 : %d점' % x)


# In[29]:


x = 85
if x >= 90:
    print("Very good")
elif  80 <= x <90:
    print("Good")
else :
    print("Bad")


# In[31]:


for a in [0, 1, 2, 3, 4, 5]:
    print(a)


# In[33]:


myFriends = ['James', 'Robert', 'Lisa', 'Mary'] # 리스트를 변수에 할당
for myFriend in myFriends:
    print(myFriend)


# In[35]:


for x in range(5) :
    print('안녕하세요.')


# In[37]:


range(5)


# In[39]:


print(range(5))


# In[41]:


print(list(range(5)))


# In[43]:


print(list(range(0, 5, 1)))


# In[46]:


print(list(range(0, 20, 5)))
print(list(range(-10, 0, 2)))
print(list(range(3, -10, -3)))
print(list(range(0, -5, 1)))


# In[48]:


for i in range(1, 11) :
    print(i, end =' ')
print()


# In[50]:


for i in range(1, 10, 2) :
    print(i, end =' ')
print()


# In[54]:


x_list = ['x1', 'x2']
y_list = ['y1', 'y2']

print("x  y")
for x in x_list:
    for y in y_list:
        print(x, y)


# In[56]:


names = ['James', 'Robert', 'Lisa', 'Mary']
scores = [95, 96, 97, 94]


# In[58]:


for k in range(len(names)):
    print(names[k], scores[k])


# In[60]:


x = 0
while x < 5 :
    print('안녕하세요')
    x += 1


# In[62]:


i = 0
sum = 0

print("i sum")
while (sum < 20):
    i = i + 1
    sum = sum + i
    print(i, sum)


# In[68]:


for k in range(10):
    if k > 2:
        break
    print(k)


# In[70]:


k = 0
while True:
    k = k + 1
    if k > 3:
        break
    print(k)


# In[72]:


for k in range(5):
    if k == 2:
        continue
    print(k, end=' ')
print()


# In[ ]:


while True:
    pass


# In[ ]:


class MyEmptyClass:
    pass


# In[ ]:




