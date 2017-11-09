
# coding: utf-8

# # HW01
# 
# ## 這個作業主要的目的是希望同學們了解善用模組跟套件可以很容易取得問題的快速解。

# ## Q1. 請使用 python 讀入 Nasdaq 公司資訊！
# 
# 提示：
# 1. 請先找到 Nasdaq Company List 的 .csv 檔的網址。
# 2. 使用 pandas 套件的 read_csv 函式來讀入 .csv 檔。

# In[6]:


import pandas as pd


# In[7]:


url="http://www.nasdaq.com/g00/3_c-6bbb.sfx78ifv.htr_/c-6RTWJUMJZX77x24myyux3ax2fx2fbbb.sfx78ifv.htrx2fx78hwjjsnslx2fhtrufsnjx78-gd-nsizx78ywd.fx78ucx3fjchmfsljx3dSFXIFVx26wjsijwx3ditbsqtfi_$/$/$"


# In[8]:


df=pd.read_csv(url)


# In[9]:


df.head()


# ## Q2. 請使用 python 畫中山大學管理學院周邊地圖！
# 
# 提示：
# 
# 1. 使用 geocoder 套件來找出地址的 GPS 座標。
# 2. 使用 folium 套件來顯示地圖。

# In[3]:


import folium


# In[5]:


import geocoder


# In[6]:


folium.Map(location=[22.627496, 120.265277],zoom_start=16)                   


# ## Q3. 請使用 python 將新聞中可能的關鍵詞萃取出來！ (Bonus)
# 
# 提示：
# 
# 1. 使用老師提供的 util.py 來擷取鉅亨網上特定新聞的內容。
# 2. 使用 jieba 套件來擷取關鍵詞。

# In[7]:


import util


# In[8]:


news_text= util.get_news_article("https://news.cnyes.com/news/id/3959659?exp=b")


# In[9]:


news_text


# In[10]:


import jieba


# In[11]:


import jieba.analyse
jieba.analyse.extract_tags(news_text,topK=20)

