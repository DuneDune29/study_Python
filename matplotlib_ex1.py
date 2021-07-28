#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


data1 = [10, 14, 19, 20, 25]


# In[3]:


plt.plot(data1)


# In[4]:


import numpy as np

x = np.arange(-4.5, 5, 0.5)
y = 2 * x ** 2
[x, y]


# In[5]:


plt.plot(x, y)
plt.show()


# In[6]:


x = np.arange(-4.5, 5, 0.5)
y1 = 2*x**2
y2 = 5*x + 30
y3 = 4*x**2 + 10


# In[7]:


plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.show()


# In[8]:


plt.plot(x, y1) # 처음 그리기 함수를 수행하면 그래프 창이 자동으로 생성됨

plt.figure() # 새로운 그래프 창을 생성함
plt.plot(x, y2) # 새롭게 생성된 그래프 창에 그래프를 그림

plt.show()


# In[9]:


x = np.arange(-5, 5, 0.1)
y1 = x**2 - 2
y2 = 20 * np.cos(x)**2

plt.figure(1) # 1번 그래프 창을 생성
plt.plot(x, y1)
plt.figure(2) # 2번 그래프 창을 생성
plt.plot(x, y2)
plt.figure(1) # 이미 생성된 1번 그래프 창을 지정
plt.plot(x, y2)
plt.figure(2) # 이미 생성된 2번 그래프 창을 지정
plt.clf() # 2번 그래프 창에 그려진 모든 그래프를 지움
plt.plot(x, y1) # 지정된 그래프 창에 그래프를 그림
plt.show()


# In[10]:


x = np.arange(0, 10, 0.1)
y1 = 0.3*(x-5)**2 + 1
y2 = -1.5*x + 3
y3 = np.sin(x)**2
y4 = 10*np.exp(-x) + 1


# In[12]:


# 2 x 2 행렬로 이뤄진 서브 그래프에서 p에 따라 위치를 지정
plt.subplot(2, 2, 1) # p는 1
plt.plot(x, y1)
plt.subplot(2, 2, 2) # p는 2
plt.plot(x, y2)
plt.subplot(2, 2, 3) # p는 3
plt.plot(x, y3)
plt.subplot(2, 2, 4) # p는 4
plt.plot(x, y4)
plt.show()


# In[13]:


x = np.linspace(-4, 4, 100)
y1 = x**3
y2 = 10*x**2 - 2

plt.plot(x, y1, x, y2)
plt.show()


# In[14]:


plt.plot(x, y1, x, y2)
plt.xlim(-1, 1)
plt.ylim(-3, 3)
plt.show()


# In[15]:


x = np.arange(0, 5, 1)
y1 = x
y2 = x + 1
y3 = x + 2
y4 = x + 3
plt.plot(x, y1, x, y2, x, y3, x, y4)
plt.show()


# In[16]:


plt.plot(x, y1, 'm', x, y2, 'y', x, y3, 'k', x, y4, 'c')
plt.show()


# In[17]:


plt.plot(x, y1, '-', x, y2, '--', x, y3, ':', x, y4, '-.')
plt.show()


# In[18]:


plt.plot(x, y1, 'o', x, y2, '^', x, y3, 's', x, y4, 'd')
plt.show()


# In[19]:


plt.plot(x, y1, '>--r', x, y2, 's-g', x, y3, 'd:b', x, y4, '-.Xc')
plt.show()


# In[20]:


x = np.arange(-4.5, 5, 0.5)
y = 2*x**3

plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()


# In[21]:


plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph title')
plt.show()


# In[22]:


plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph title')
plt.grid(True) # plt.grid() 도 가능


# In[23]:


x = np.arange(0, 5, 1)
y1= x
y2= x + 1
y3= x + 2
y4= x + 3


# In[24]:


plt.plot(x, y1, '>--r', x, y2, 's-g', x, y3, 'd:b', x, y4, '-.Xc')
plt.legend(['data1', 'data2', 'data3', 'data4'])
plt.show()


# In[26]:


import matplotlib.pyplot as plt
import numpy as np


# In[27]:


plt.plot(x, y1, '>--r', x, y2, 's-g', x, y3, 'd:b', x, y4, '-.Xc')
plt.legend(['data1', 'data2', 'data3', 'data4'], loc = 'lower right')
plt.show()


# In[28]:


import matplotlib

matplotlib.rcParams['font.family'] = 'Malgun Gothic' # '맑은 고딕'으로 설정
matplotlib.rcParams['axes.unicode_minus'] = False


# In[29]:


plt.plot(x, y1, '>--r', x, y2, 's-g', x, y3, 'd:b', x, y4, '-.Xc')
plt.legend(['데이터1', '데이터2', '데이터3', '데이터4'], loc = 'best')
plt.xlabel('X 축')
plt.ylabel('Y 축')
plt.title('그래프 제목')
plt.grid(True)


# In[30]:


import matplotlib.pyplot as plt

height = [165, 177, 160, 180, 185, 155, 172] # 키 데이터
weight = [62, 67, 55, 75, 90, 43, 64] # 몸무게 데이터

plt.scatter(height, weight)
plt.xlabel('Height(m)')
plt.ylabel('Weight(Kg)')
plt.title('Height & Weight')
plt.grid(True)


# In[31]:


plt.scatter(height, weight, s=500, c='r') # 마커 크기는 500, 컬러는 붉은색(red)
plt.show()


# In[32]:


city = ['서울', '인천', '대전', '대구', '울산', '부산', '광주']
# 위도(latitude)와 경도(longitude)
lat = [37.56, 37.45, 36.35, 35.87, 35.53, 35.18, 35.16]
lon = [126.97, 126.70, 127.38, 128.60, 129.31, 129.07, 126.85]
# 인구 밀도(명/km^2): 2017년 통계청 자료
pop_den = [16154, 2751, 2839, 2790, 1099, 4454, 2995]

size = np.array(pop_den) * 0.2 # 마커의 크기 지정
colors = ['r', 'g', 'b', 'c', 'm', 'k', 'y'] # 마커의 컬러 지정
plt.scatter(lon, lat, s=size, c=colors, alpha=0.5)
plt.xlabel('경도(longitude)')
plt.ylabel('위도(latitude)')
plt.title('지역별 인구 밀도(2017)')

for x, y, name in zip(lon, lat, city):
    plt.text(x,y, name) # 위도 경도에 맞게 도시 이름 출력
plt.show()


# In[33]:


member_IDs = ['m_01', 'm_02', 'm_03', 'm_04'] # 회원 ID
before_ex = [27, 35, 40, 33] # 운동 시작 전
after_ex = [30, 38, 42, 37] # 운동 한달 후


# In[34]:


n_data = len(member_IDs) # 회원이 네 명이므로 전체 데이터 수는 4
index = np.arange(n_data) #NumPy를 이용해 배열 생성(0,1, 2, 3)
plt.bar(index, before_ex) # bar(x,y)에서 x=index, height=before_ex 로 지정
plt.show()


# In[35]:


barWidth = 0.4
plt.bar(index, before_ex, color='c', align='edge', width = barWidth,
       label = 'before')
plt.bar(index + barWidth, after_ex, color='m', align='edge',
       width = barWidth, label='after')

plt.xticks(index + barWidth, member_IDs)
plt.legend()
plt.xlabel('회원 ID')
plt.ylabel('윗몸일으키기 횟수')
plt.title('운동 시작 전과 후의 근지구력(복근) 변화 비교')
plt.show()


# In[36]:


fruit = ['사과', '바나나', '딸기', '오렌지', '포도']
result = [7, 6, 3, 2, 2]


# In[37]:


plt.pie(result)
plt.show()


# In[38]:


plt.figure(figsize=(5,5))
plt.pie(result, labels=fruit, autopct='%.1f%%')
plt.show()


# In[39]:


explode_value = (0.1, 0, 0, 0, 0)

plt.figure(figsize=(5,5))
plt.pie(result, labels=fruit, autopct='%.1f%%', startangle=90,
       counterclock = False, explode=explode_value, shadow=True)
plt.show()


# In[40]:


import pandas as pd

temperature = [25.2, 27.4, 22.9, 26.2, 29.5, 33.1, 30.4, 36.1, 34.4, 29.1]
Ice_cream_sales = [236500, 357500, 203500, 365200, 446600, 574200, 453200,
                  675400, 598400, 463100]

dict_data = {'기온':temperature, '아이스크림 판매량':Ice_cream_sales}
df_ice_cream = pd.DataFrame(dict_data, columns = ['기온', '아이스크림 판매량'])
df_ice_cream


# In[42]:


df_ice_cream.plot.scatter(x='기온', y='아이스크림 판매량', grid=True,
                         title='최고 기온과 아이스크림 판매량')
plt.show()


# In[ ]:




