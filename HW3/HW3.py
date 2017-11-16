
# coding: utf-8

# In[2]:


import requests                        #BeautifulSoup是用來擷取網頁資訊的 Python 函式庫。
from bs4 import BeautifulSoup


# In[3]:


url = "http://news.cnyes.com/Content/20151214/20151214080543107512510.shtml?c=headline"


# In[4]:


r = requests.get(url)        #以某種 HTTP 方法向遠端服務器發送一個请求，得到一个個Response 的结果，並命名為 r，將r以UTF-8重新編碼。
r.encoding = "UTF-8"


# In[5]:


soup = BeautifulSoup(r.text,"lxml")         #把r用BeautifulSoup函式庫取出並命名為soup，並使用lxml讀入，然後印出soup。
print(soup)


# In[10]:


news_text = soup.select('div[itemprop="articleBody"]')[0].text   #搜尋文章主體，並印出news_text 
print(news_text)


# In[11]:


news_summary = soup.p.string    #找出原文的摘要，並印出news_summary
print(news_summary)


# In[12]:


import jieba                   #載入結巴套件和jieba.analyse套件
import jieba.analyse


# In[24]:


jieba.set_dictionary('dict.txt.big')   #利用結巴的字典


# In[25]:


keywords = jieba.analyse.extract_tags(news_text, topK=10, withWeight=False)    
#選出新聞內容出現機率前10高的關鍵字


# In[20]:


print("/ ".join(keywords))      #印出前十個關鍵字


# In[23]:


#用repr的函式將挑選出來的10個關鍵字的機率列出
print(repr(jieba.analyse.extract_tags(news_text, topK=10, withWeight=True)))


# In[26]:


print(repr(jieba.analyse.textrank(news_text, topK=10, withWeight=True)))


# In[27]:


#定義關鍵字的函式,利用for迴圈，使用enumerate(), 傳回一個次序及值成組tuple
def index_of_keyword(sentences, keyword):
    for i, s in enumerate(sentences):
        if keyword in s:
              return i
    return -1


# In[28]:


#刪除格行,並用句號分開,顯示出有多少句子
sentences = news_text.replace("\n","").split(u"。")
len(sentences)


# In[29]:


#利用迴圈顯示出13行句子
for sentence in sentences:
    print(sentence + u"。")


# In[30]:


#利用關鍵字索引,sentences與紫光為兩個變數,最後顯示出紫光在第7行。第一句記為第0行。
index_of_keyword(sentences,u"紫光")


# In[31]:


#顯示出第7行的內容,並加入句號。
print(sentences[index_of_keyword(sentences,u"紫光")]+u"。")


# In[32]:


#第0句有64個字(包含數字及標點符號)。
len(sentences[0])


# In[33]:


#建立新的list,利用迴圈搜尋前3個關鍵字在哪個句子,加入新的list中。
s_index = []
for keyword in keywords[:3]:
    s_index.append(index_of_keyword(sentences,keyword))
#並將得到的句子轉成索引值
s_set = set(s_index)
s_index = list(s_set)


# In[34]:


#建立新的字串,用找好的索引值回傳到sentences,列出句子,並加上句號。
summary = ""
for i in s_index:
    summary += sentences[i]+u"。"


# In[35]:


#印出最後摘要的新聞內容。
print(summary)


# In[36]:


#印出原文的新聞摘要。
print(news_summary)

