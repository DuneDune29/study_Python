#!/usr/bin/env python
# coding: utf-8

# In[1]:


coffee_menu_str = "에스프레소, 아메리카노, 카페라떼, 카포치노"
coffee_menu_str.split(',')


# In[2]:


"  에스프레소  \n\n  아메리카노  \n  카페라테  카푸치노  \n\n".split()


# In[3]:


"에스프레소 아메리카노 카페라테 카푸치노".split(maxsplit=2)


# In[4]:


phone_number = "+82-01-2345-6789" # 국가 번호가 포함된 전화번호
split_num = phone_number.split("-", 1) # 국가 번호와 나머지 번호 분리

print(split_num)
print("국내전화번호: {0}".format(split_num[1]))


# In[5]:


test_str = "aaabbPythonbbbaa"
temp1 = test_str.strip('a') # 문자열 앞뒤의 'a' 제거
temp1


# In[6]:


temp1.strip('b') 


# In[7]:


test_str_multi = "##***!!!###....  Python is powerful.!...  %%!#..   "
test_str_multi.strip('*.#! %')


# In[8]:


"\n This is very \n fast. \n\n".strip()


# In[9]:


coffee_menu = "  에스프레소, 아메리카노,     카페라테    , 카푸치노  "
coffee_menu_list = coffee_menu.split(',')

coffee_list = [] # 빈 리스트 생성
for coffee in coffee_menu_list:
    temp = coffee.strip() # 문자열의 공백 제거
    coffee_list.append(temp) # 리스트 변수에 추가
    
print(coffee_list) # 최종 리스트 출력


# In[10]:


address_list = ["서울시", "서초구", "반포대로", "201(반포동)"]
" ".join(address_list)


# In[11]:


str_f = "Python code."

print("찾는 문자열의 위치:", str_f.find("Python"))
print("찾는 문자열의 위치:", str_f.find("code"))
print("찾는 문자열의 위치:", str_f.find("n"))
print("찾는 문자열의 위치:", str_f.find("easy"))


# In[12]:


str_f_se = "Python is powerful. Python is easy to learn."

print(str_f_se.find("Python", 10, 30)) # 시작 위치(strat)와 끝 위치(end) 지정
print(str_f_se.find("Python", 35)) # 찾기 위한 시작 위치(start) 지정


# In[13]:


str_se = "Python is powerful. Python is easy to learn."

print("Python으로 시작?:", str_se.startswith("Python"))
print("is로 시작?:", str_se.startswith("is"))
print(".로 끝?:", str_se.endswith("."))
print("learn으로 끝?:", str_se.endswith("learn"))


# In[14]:


str_a = 'Python is fast. Python is friendly. Python is open.'
print(str_a.replace('Python', 'IPython'))
print(str_a.replace('Python', 'IPython', 2))


# In[15]:


print('abc1234'.isalnum()) # 특수 문자나 공백이 아닌 문자와 숫자로 구성됨
print('   abc1234'.isalnum()) # 문자열에 공백이 있음
print('   '.isspace()) # 문자열이 공백으로만 구성됨
print(' 1 '.isspace()) # 문자열에 공백 외에 다른 문자가 있음


# In[16]:


get_ipython().run_cell_magic('writefile', 'D:\\pywork\\my_first_module.py', '# File name: my_first_module.py\n\ndef my_function():\n    print("This is my first module.")')


# In[17]:


get_ipython().system('type D:\\pywork\\my_first_module.py')


# In[18]:


cd D:\pywork


# In[20]:


import my_first_module

my_first_module.my_function()


# In[21]:


import random

random.random()


# In[22]:


import random

dice1 = random.randint(1, 6) # 임의의 정수가 생성됨
dice2 = random.randint(1, 6) # 임의의 정수가 생성됨
print('주사위 두 개의 숫자: {0}, {1}'.format(dice1, dice2))


# In[23]:


import random

num1 = random.randrange(1, 10, 2) # 1 ~ 9(10-1) 중 임의의 홀수 선택
num2 = random.randrange(0, 100, 10) # 10~ 99(100-1) 중 임의의10의 단위 숫자 선택
print('num1: {0}, num2: {1}'.format(num1, num2))


# In[24]:


import random

menu = ['비빔밥', '된장찌개', '볶음밥', '불고기', '스파게티', '피자', '탕수육']
random.choice(menu)


# In[28]:


import random

random.sample([1, 2, 3, 4, 5], 2) # 모집단에서 두 개의 인자 선택


# In[30]:


import datetime

set_day = datetime.date(2019, 3 ,1)
print(set_day)


# In[31]:


import datetime

day1 = datetime.date(2019, 4, 1)
day2 = datetime.date(2019, 7, 10)
diff_day = day2 - day1
print(diff_day)


# In[32]:


import datetime

today = datetime.date.today()
special_day = datetime.date(2021, 4, 12)
print(special_day - today)


# In[33]:


import datetime

set_time = datetime.time(15, 30, 45)
print(set_time)


# In[34]:


import datetime

set_dt = datetime.datetime(2018, 10, 9, 10, 20, 0)
print(set_dt)


# In[35]:


from datetime import date, time, datetime

print(datetime.now())


# In[37]:


import calendar

print(calendar.calendar(2021))


# In[ ]:




