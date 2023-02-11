# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 16:17:32 2023

@author: Administrator
"""

# 1、导入模块

import requests
from bs4 import BeautifulSoup

# 2、定义 url 和请求头参数
url = 'https://s.weibo.com/top/summary/'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "cookie": "SUB=_2AkMUnjXgf8NxqwFRmP8WyWvjZY52zQzEieKiwsQ7JRMxHRl-yT9kqlE4tRB6Px4bDzSHkzvBITl5nmzLFI-JI2GggfEi; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWOgaE_-ubyxa7KFL77lwXu; _s_tentry=weibo.com; Apache=2054102635892.19.1673709436498; SINAGLOBAL=2054102635892.19.1673709436498; ULV=1673709436566:1:1:1:2054102635892.19.1673709436498:",
}

# 3、requests 发送 html 请求，获取 html 字符串
response = requests.get(url, headers=headers)
content = response.content.decode('utf8')

# 4、实例化 BeautifulSoup 对象（中介）
soup = BeautifulSoup(content, 'lxml')

# 5、获取数据
tds = soup.find_all('td', class_ = "td-02")[1:]
sinas = []
for td in tds:
    # 热搜内容
    event = td.find_all('a')[0].string

    # 热度
    hot = td.find_all('span')[0].string

    sina = {
        "热搜": event,
        "热度": hot,
    }

    sinas.append(sina)
# 6、存储数据
print(sinas)
