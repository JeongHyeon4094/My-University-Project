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


# In[2]:


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


# In[3]:


print("==========국 내 발 생 인 원==========")
print(now_time.text, "기준\n")
now_inter_in = soup.select("span", {"class":"data"})
print("국내 발생", now_inter_in[13].text, "명")
print("해외 발생", now_inter_in[15].text, "명")


# In[4]:


print("==========종 합 확 진 환 자==========")
print("확진환자", now_inter_in[16].text, "명")
print(now_inter_in[18].text, "\n")
print("격리 해제", now_inter_in[19].text)
print("전일 대비", now_inter_in[20].text, "\n")
print("현재 확진환자", now_inter_in[22].text)
print("전일 대비", now_inter_in[23].text, "\n")
print("사 망", now_inter_in[25].text)
print("전일 대비", now_inter_in[26].text, "\n")


# In[5]:


print("==========검  사  현  황==========\n")
print("누적 검사수", now_inter_in[31].text)
print("누적 검사완료수", now_inter_in[33].text)
print("누적 확진율", now_inter_in[35].text)


# In[ ]:


from flask import Flask, render_template

#플라스크 객체 생성
app = Flask(__name__)

#라우팅 경로 요청 시 실행 함수
@app.route("/covid")
def covid19():
    now_time = soup.find("span", {"class":"livedate"})
    table = soup.find("div", {"class":"open"})
    p = table.find_all("p")
    now_inter_in = soup.select("span", {"class":"data"})
    now_t = now_time.text  #누계 시간 nt
    
    Four_sta = p[0].text  #4단계 fs
    Three_sta = p[1].text  #3단계 ts
    Two_sta = p[2].text  #2단계 tws
    One_sta = p[3].text  #1단계 os
    
    in_sta = now_inter_in[13].text  #국내확진 ins
    out_sta = now_inter_in[15].text  #입국확진 outs
    
    covid_a = now_inter_in[16].text  #코로나 전체 ca
    covid_a_n = now_inter_in[18].text  #코로나 전체 전일 can
    covid_b = now_inter_in[19].text  #코로나 해체 cb
    covid_b_n = now_inter_in[20].text  #코로나 해제 전일 cbn
    covid_now = now_inter_in[22].text  #코로나 확진 cn
    covid_now_n = now_inter_in[23].text  #코로나 확진 전일cnn
    covid_d = now_inter_in[25].text  #코로나 사망 cd
    covid_d_n = now_inter_in[26].text  #코로나 사망 전일 cdn
    
    covid_c = now_inter_in[31].text  #코로나 검사수 cc
    covid_c_o = now_inter_in[33].text  #코로나 검사 완료수 cco
    covid_in = now_inter_in[35].text  #코로나 확진율 cin
    return render_template("covid19.html", nt = now_t, fs = Four_sta, ts = Three_sta, tws = Two_sta, os = One_sta, ins = in_sta, outs = out_sta, ca = covid_a, can = covid_a_n, cb = covid_b, cbn = covid_b_n, cn = covid_now, cnn = covid_now_n, cd = covid_d, cdn = covid_d_n, cc = covid_c, cco = covid_c_o, cin = covid_in)

if __name__ == "__main__":
    app.run()


# In[ ]:




