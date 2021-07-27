#!/usr/bin/env python
# coding: utf-8

# In[4]:


def my_func():
    print("My first function!")
    print("This is a function.")


# In[6]:


my_func()


# In[9]:


def my_calc(x,y):
    z = x * y
    return z


# In[11]:


my_calc(3,4)


# In[12]:


a = 5 # 전역 변수

def func1():
    a = 1 # 지역 변수. func1()에서만 사용
    print("[func1] 지역 변수 a =", a)
    
def func2():
    a = 2 # 지역 변수. func2()에서만 사용
    print("[func2] 지역 변수 a =", a)
    
def func3():
    print("[func3] 전역 변수 a =", a)
    
def func4():
    global a # 함수 내에서 전역 변수 변경 위해 선언
    a = 4     # 전역 변수. func1()에서만 사용
    print("[func1] 전역 변수 a =", a)


# In[13]:


func1() #함수 func1() 호출
func2() #함수 func1() 호출
print("전역 변수 a =", a) # 전역 변수 출력


# In[14]:


func3()
func4()
func3()


# In[16]:


def average(*scores) :
    sum = 0
    for i in range(len(scores)) :
        sum += scores[i]
    avg = sum/len(scores)
    print('%d과목의 평균 : %.2f' % (len(scores), avg))
average(80, 90, 100)
average(75, 80, 94, 78)
average(80, 73, 76, 86, 82)


# In[18]:


def func(x) :
    x = 100
    print('func() : x =', x, ', id =', id(x))

x = 10
print('x = ', x, ', id =', id(x))
func(x)
print('x = ', x, ', id =', id(x))


# In[19]:


myNum = [10, 5, 12, 0, 3.5, 99.5, 42]
[min(myNum), max(myNum)]


# In[20]:


myStr = 'zxyabc'
[min(myStr), max(myStr)]


# In[21]:


sumList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum(sumList)


# In[22]:


scores = [90, 80, 95, 85]
print("총점:{0}, 평균:{1}". format(sum(scores), sum(scores)/len(scores)))


# In[ ]:




