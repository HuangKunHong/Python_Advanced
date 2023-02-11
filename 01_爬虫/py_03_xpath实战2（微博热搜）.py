# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 22:20:24 2023

@author: Administrator
"""

# 1、导入必要的库或模块
import requests
from lxml import etree


# 2、定义网页和请求头
url = "https://s.weibo.com/top/summary/"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
           "cookie": "SUB=_2AkMUnjXgf8NxqwFRmP8WyWvjZY52zQzEieKiwsQ7JRMxHRl-yT9kqlE4tRB6Px4bDzSHkzvBITl5nmzLFI-JI2GggfEi; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWOgaE_-ubyxa7KFL77lwXu; _s_tentry=weibo.com; Apache=2054102635892.19.1673709436498; SINAGLOBAL=2054102635892.19.1673709436498; ULV=1673709436566:1:1:1:2054102635892.19.1673709436498:",
           }


# 3、获取 html 页面（注意编码和转码的问题）
response = requests.get(url, headers = headers)
content =  response.content.decode('utf-8')

print(content)
# 4、etree 解析
html = etree.HTML(content)

# 5、观察网页源码，查看标签特征
# 6、编写 xpath 语法，获取标签内容（文本信息末尾添加 / text()）
# 7、存储数据（ zip 函数双循环）

# 1> 方法一
trendings = html.xpath('//tbody/tr[position()>1]//a/text()')
clouts = html.xpath('//tbody/tr[position()>1]//span/text()')


H = []

for trending,clout in zip(trendings, clouts):
    dic = {}
    dic = {
        "热搜":trending,
        "热度":clout,
        }
    
    H.append(dic)
    
print(H)

# 2> 方法二
trs = html.xpath("//tbody/tr[position()>1]")
H = []
for tr in trs:
    dic = {}
    trending = tr.xpath('.//a/text()')[0]
    clout = tr.xpath('.//span/text()')[0]
    dic = {
        "热搜": trending,
        "热度": clout,
        }
    H.append(dic)

print(H)