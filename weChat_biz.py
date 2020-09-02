#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import selenium
import time
import re
import requests
from readFile import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 获取微信公众Biz
def weChatBiz():
    # 读取txt文档但不读取文档的抬头，把位置为在最左的字串更换为list数据格式
    wechatlist = readFile()[0].tolist()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=400,600')

    #创建两个新变量
    name = []
    biz = []

    for i in wechatlist:
        browser = webdriver.Chrome(options=chrome_options, executable_path=".chrome/chromedriver.exe")
        url = 'https://weixin.sogou.com/weixin?type=1&s_from=input&query='+ i +'&ie=utf8&_sug_=n&_sug_type_='
        # 打开浏览器预设网址
        browser.get(url)
        urls = browser.find_elements_by_xpath("//a")
        window_before = browser.window_handles[0]

        time.sleep(0.5)

        if (urls[17] is not None) and (urls[17].get_attribute("href") != "javascript:void(0);") :
            urls[17].click()
            window_after = browser.window_handles[1]
            browser.switch_to_window(window_after)

            time.sleep(0.5)

            res3 = requests.get(browser.current_url)
            a = re.findall('var biz = "(\w+==)',res3.text)
            b = re.findall('var title ="([a-zA-Z0-9_\u4e00-\u9fa5]+)', res3.text)
            biz.append(a)
            name.append(b)

        else:
            a = []
            b = []
            biz.append(a)
            name.append(b)

        browser.quit()
        print(a, b)

    final=pd.DataFrame((pd.Series([x[0] if len(x[:])!=0 else x[:] for x in name]),pd.Series([y[0] if len(y[:])!=0 else y[:] for y in biz]))).T
    final.to_excel(BASE_DIR + "\微信biz.xlsx", header=["name", "biz"], index=False)

