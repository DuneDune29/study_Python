#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

word_count_file = "D:/pywork/word_count.csv"
word_count = pd.read_csv(word_count_file, index_col = '단어')
word_count.head(5)


# In[2]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt

korean_font_path = 'C:/Windows/Fonts/malgun.ttf'


# In[6]:


# 워드 클라우드 이미지 생성
wc = WordCloud(font_path=korean_font_path, background_color='white')

frequencies = word_count['빈도'] # pandas의 Series 형식
wordcloud_image = wc.generate_from_frequencies(frequencies)


# In[7]:


# 생성한 워드 클라우드 이미지를 화면에 표시
plt.imshow(wordcloud_image, interpolation="bilinear")
plt.axis("off")
plt.show()


# In[ ]:




