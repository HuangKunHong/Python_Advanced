# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests

# http常见请求：GET POST

# 访问的网页地址
url = "https://cn.bing.com/search"
keyword = {
    "q":"番茄"
    }
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54",

    
    }
# 响应
response = requests.get(url, params= keyword, headers=headers)
# print(type(response))
# 查询网页解码方式
# print(response.encoding)
# 查询网页响应状态
# print(response.status_code)

# 获取网页html内容的有两种方式response.text 和 response.content.decode('utf-8')
# response.text 有python猜测网页的编码方式，可能尝试乱码，response.content.decode('utf-8')可以指定编码方式
# print(response.text)

html_data = response.content.decode('utf-8')
print(html_data)

print(response.url)
