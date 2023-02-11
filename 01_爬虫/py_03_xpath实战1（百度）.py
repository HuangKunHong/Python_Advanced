# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 21:44:16 2023

@author: Administrator
"""

# 1、导入必要的库或模块
import requests
from lxml import etree


# 2、定义网页和请求头
url = "https://www.baidu.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}


# 3、获取 html 页面（注意编码和转码的问题）
response = requests.get(url, headers = headers)
content = response.content.decode('utf8')

# 4、etree 解析
html = etree.HTML(content)


# 5、观察网页源码，查看标签特征
# 6、编写 xpath 语法，获取标签内容（文本信息末尾添加 / text()）
contents = html.xpath('//div[@id = "s-top-left" ]/a/text()')
print(contents)

urls = html.xpath('//div[@id = "s-top-left" ]/a/@href')
print(urls)

# 7、存储数据（ zip 函数双循环）
baidu = []

for content,url in zip(contents, urls):
    eg = {}
    eg = {
        "content": content,
        "url": url,
        }
    baidu.append(eg)
    
print(baidu)
    
