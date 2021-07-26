#!/usr/bin/env python
# coding: utf-8

# In[2]:


list_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_data)
print(list_data[0:3])
print(list_data[4:8])
print(list_data[:3])
print(list_data[7:])
print(list_data[::2])


# In[4]:


print(list_data)
del list_data[6]
print(list_data)


# In[6]:


list_data1 = [1, 2, 3, 4, 5]
print(5 in list_data1)
print(6 in list_data1)


# In[8]:


list_data1


# In[10]:


print(list_data1)


# In[11]:


list_data1 = [1, 2, 3, 4, 5]


# In[13]:


myFriends = ['James', 'Robert', 'Lisa', 'Mary']
print(myFriends)
myFriends.append('Thomas')
print(myFriends)


# In[15]:


myFriends.insert(1, 'Paul')
print(myFriends)


# In[17]:


myFriends = ['James', 'Robert', 'Lisa', 'Mary']
myFriends.append(['Laura', 'Betty'])
print(myFriends)


# In[19]:


myFriends = ['James', 'Robert', 'Lisa', 'Mary']
myFriends.extend(['Laura', 'Betty'])
print(myFriends)


# In[27]:


a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
a.pop(3) # del a[3]와 동일
print(a)


# In[28]:


a.remove(90)
print(a)


# In[31]:


a.clear()
print(a)


# In[1]:


list1 = ['a', 'bb', 'c', 'd', 'aaa', 'c', 'ddd', 'aaa', 'b', 'cc', 'd', 'aaa', ]
length = list1.count('aaa')
print(length)


# In[3]:


print(len(list1))


# In[5]:


list2 = [-7, 1, 5, 8, 3, 9, 11, 13]
list2.sort()
print(list2)


# In[7]:


list2.sort(reverse=True)
print(list2)


# In[9]:


nums = [[10, 20, 30], [40, 50, 60]]
print(nums[0])
print(nums[1])
print(nums[0][1])
print(nums[1][2])


# In[11]:


nums


# In[13]:


tuple5 = (1, 2, 3, 4)
type(tuple5)


# In[15]:


tuple5[1] = 5 # 튜플의 요소는 변경 불가


# In[17]:


del tuple5[1]


# In[19]:


tuple7 = ('a', 'a', 'a', 'b', 'b', 'c', 'd')
tuple7.count('a')


# In[21]:


set1 = {1, 2, 3}
set1a = {1, 2, 3, 3}
print(set1)
print(set1a)


# In[23]:


print(type(set1))


# In[25]:


a = [1, 2, 3, 4, 5]
type(a)


# In[28]:


b = tuple(a)
b


# In[30]:


type(b)


# In[32]:


c = set(a)
c


# In[34]:


type(c)


# In[36]:


a


# In[38]:


list(c)


# In[40]:


c


# In[42]:


country_capital = {"영국":"런던", "프랑스":"파리", "스위스":"베른",
                   "호주":"멜버른", "덴마크":"코펜하겐"}
country_capital


# In[44]:


type(country_capital)


# In[47]:


dict_data2 = {1:10, 2:20, 3:30, 4:40, 5:50}
print(dict_data2)
print(dict_data2[4])


# In[49]:


mixed_dict = {1:10, 'dict_num': {1:10, 2:20},
            "dict_list_tuple": {"A":[11, 12, 13], "B":(21, 22, 23)},
             "dict_string": "이것은 책입니다."}
mixed_dict


# In[51]:


country_capital


# In[53]:


country_capital["독일"]= "베를린"
country_capital


# In[55]:


country_capital["호주"]= "캔버라"
country_capital


# In[57]:


fruit_code = {"사과":101, "배":102, "딸기":103, "포도":104, "바나나":105}


# In[59]:


print(fruit_code.keys())


# In[61]:


print(fruit_code.values())


# In[63]:


fruit_code.items()


# In[65]:


list(fruit_code.items())


# In[78]:


fruit_code2 = {"오렌지":106, "수박":107}


# In[79]:


fruit_code.update(fruit_code2)
fruit_code


# In[80]:


del fruit_code2['수박']


# In[82]:


fruit_code2


# In[83]:


phones = {'갤럭시 노트8': 2017, '갤럭시 S9': 2018, 
        '갤럭시 노트10': 2019, '갤럭시 S20': 2020}
print(phones)
for key in phones :
     print('%s => %s' % (key, phones[key]))
print(len(phones))

