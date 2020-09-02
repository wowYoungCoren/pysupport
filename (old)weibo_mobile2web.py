#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd 
import requests
import re

#用pandas包里专门读取excel下的各类文档类型的功能读取文档，并把‘链接’转为list数据类型
df1=pd.read_excel("weibo(old).xlsx")
urllist=df1.链接.tolist()

list=[]

for i in urllist:
    res = requests.get(i)
    uid=re.search(r'"uid": (\d+)', res.text).group(1)
    bid=re.search(r'"bid": "([A-Za-z0-9]+)', res.text).group(1)
    url="https://weibo.com/"+uid+"/"+bid
    list.append(url)

    
#输出保存为"hehe.csv"同时不带有列抬头
pd.DataFrame(list).to_csv("hehe(old).csv", header=None, index=False)

