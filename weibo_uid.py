#!/usr/bin/env python
# coding: utf-8

import re
import requests
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from readFile import *

def weiboUID():
    option=webdriver.ChromeOptions()
    # option.add_argument('headless') # 设置option
    driver = webdriver.Chrome(options=option, executable_path=".chrome/chromedriver.exe")  # 调用带参数的谷歌浏览器
    driver.get('https://weibo.com/')
    print('正在加载界面....')
    time.sleep(1)

    WebDriverWait(driver, 20, 0.5).until(EC.visibility_of_element_located((By.ID, 'loginname'))).send_keys('13676010298')

    driver.find_element_by_name('password').send_keys('Yk970716!')
    driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a/span').click()
    time.sleep(1)




    WebDriverWait(driver,100,0.5).until(EC.visibility_of_element_located((By.CLASS_NAME,'B_index')))

    #获取cookies
    cookies = driver.get_cookies()
    #创建名为“cookie_list"的array
    cookie_list=[]

    for dict in cookies:
        cookie = dict['name'] + '=' + dict['value']
        cookie_list.append(cookie)
        cookie2 = ';'.join(cookie_list)

    cookies = {i.split("=")[0]:i.split("=")[1] for i in cookie2.split(";")}

    driver.close()

    #读取指定的xlsx文档
    weibolist=pd.read_excel("转uid和biz.xlsx",sheet_name=0)
    weibolist=weibolist.KOL.tolist()

    weibo_uid=[]
    weibo_name=[]

    print("当前查询微博为")
    print("    ")

    #循环每行数据的第30-45字符并命名为“res”
    for i in weibolist[30:45]:
        res=requests.get("https://s.weibo.com/user?q="+i+"&Refer=index")
        website=re.search("//weibo.com/([/a-zA-Z0-9_\u4e00-\u9fa5]+)",res.text).group(0)
        res2=requests.get("https:"+website,cookies=cookies)
        a=re.findall("fuid=(\d+)&",res2.text)
        b=re.findall("&fname=([-a-zA-Z0-9_\u4e00-\u9fa5]+)&",res2.text)
        weibo_uid.append(a)
        weibo_name.append(b)
        print(i+"                ",end="\r")
        time.sleep(2)


    #储存到dataframe里然后再输出到"d:/weibo.xlsx"，同时保留“name”、“uid”两列的列名称
    conseq=pd.DataFrame((pd.Series([x[0] if len(x[:])!=0 else x[:] for x in weibo_name]),pd.Series([y[0] if len(y[:])!=0 else y[:] for y in weibo_uid]))).T
    conseq.to_excel(BASE_DIR + "weibo_uid.xlsx", index=False, header=["name","uid"])

    #告诉console任务完成
    print("    ")
    print("已完成所有搜索")


if __name__ == '__main__':
    weiboUID()