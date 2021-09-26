#!/usr/bin/env python
# coding: utf-8

# In[1]:


#20214094 박정현

import urllib.request
from bs4 import BeautifulSoup

url = "http://ncov.mohw.go.kr/"
page = urllib.request.urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

print("==========누 계 기 록 시 간==========\n")
now_time = soup.find("span", {"class":"livedate"})
print("코로나 현황", now_time.text)


# In[8]:


table = soup.find("div", {"class":"open"})
p = table.find_all("p")
print("==========거 리 두 기 지 역==========\n")
print("4단계 지역====================")
print(p[0].text)
print("3단계 지역====================")
print(p[1].text)
print("2단계 지역====================")
print(p[2].text)
print("1단계 지역====================")
print(p[3].text)


# In[4]:


print("==========국 내 발 생 인 원==========")
print(now_time.text, "기준\n")
now_inter_in = soup.select("span", {"class":"data"})
print("국내 발생", now_inter_in[13].text, "명")
print("해외 발생", now_inter_in[15].text, "명")


# In[5]:


print("==========종 합 확 진 환 자==========")
print("확진환자", now_inter_in[16].text, "명")
print(now_inter_in[18].text, "\n")
print("격리 해제", now_inter_in[19].text)
print("전일 대비", now_inter_in[20].text, "\n")
print("현재 확진환자", now_inter_in[22].text)
print("전일 대비", now_inter_in[23].text, "\n")
print("사 망", now_inter_in[25].text)
print("전일 대비", now_inter_in[26].text, "\n")


# In[6]:


print("==========검  사  현  황==========\n")
print("누적 검사수", now_inter_in[31].text)
print("누적 검사완료수", now_inter_in[33].text)
print("누적 확진율", now_inter_in[35].text)


# In[ ]:




