#!/usr/bin/env python
# coding: utf-8

# In[1]:


import webbrowser

url = 'www.naver.com'
webbrowser.open(url)


# In[2]:


import requests

r = requests.get("https://www.google.co.kr")
r


# In[3]:


r.text[0:100]


# In[4]:


from bs4 import BeautifulSoup

# 테스트용 html 코드
html = """<html><body><div><span>        <a href=http://www.naver.com>naver</a>        <a href=https://www.google.com>google</a>        <a href=http://www.daum.net>daum</a>        </span></div></body></html>"""

# BeautifulSoup를 이용해 HTML 소스를 파싱
soup = BeautifulSoup(html, 'lxml')
soup


# In[5]:


soup.find('a')


# In[6]:


soup.find('a').get_text()


# In[7]:


soup.find_all('a')


# In[8]:


site_names = soup.find_all('a')
for site_name in site_names:
    print(site_name.get_text())


# In[9]:


html2 = """
<html>
  <head>
    <title>작품과 작가 모음</title>
  </head>
  <body>
    <h1>책 정보</h1>
    <p id="book_title">토지</p>
    <p id="author">박경리</p>
    
    <p id="book_title">태백산맥</p>
    <p id="author">조정래</p>
    
    <p id="book_title">감옥으로부터의 사색</p>
    <p id="author">신영복</p>
 </body>
</html>
"""

soup2 = BeautifulSoup(html2, "lxml")


# In[10]:


soup2.title


# In[11]:


soup2.body


# In[12]:


soup2.body.h1


# In[13]:


soup2.find('p', {"id":"book_title"})


# In[14]:


soup2.find_all('p', {"id":"book_title"})


# In[15]:


book_titles = soup2.find_all('p', {"id":"book_title"})
authors = soup2.find_all('p', {"id":"author"})

for book_title, author in zip(book_titles, authors):
    print(book_title.get_text() + '/' + author.get_text())


# In[16]:


soup2.select('body p')


# In[17]:


soup2.select('p#book_title')


# In[18]:


import requests
from bs4 import BeautifulSoup

url = "https://www.alexa.com/topsites/countries/KR"

html_website_ranking = requests.get(url).text
soup_website_ranking = BeautifulSoup(html_website_ranking, "lxml")

# p 태그의 요소 안에서 a 태그의 요소를 찾음
website_ranking = soup_website_ranking.select('p a')


# In[19]:


website_ranking[0:6]


# In[20]:


website_ranking_address = [website_ranking_element.get_text() for website_ranking_element in website_ranking]

print("[Top Sites in South Korea]")
for k in range(6):
    print("{0}: {1}". format(k+1, website_ranking_address[k]))


# In[22]:


import pandas as pd

website_ranking_dict = {'Website': website_ranking_address}
df = pd.DataFrame(website_ranking_dict, columns=['Website'],
                 index=range(1, len(website_ranking_address)+1))
df[0:6]


# In[23]:


import requests
from bs4 import BeautifulSoup

url = "http://music.naver.com/listen/history/index.nhn?type=TOTAL&year=2021&month=2&week=1"
html_music = requests.get(url).text
soup_music = BeautifulSoup(html_music, "lxml")
soup_music


# In[ ]:




