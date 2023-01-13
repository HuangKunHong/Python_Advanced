# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests

# http常见请求：GET POST

# 访问的网页地址
url = "https://www.baidu.com/"
# 响应
response = requests.get(url)
print(type(response))
# 查询网页解码方式
print(response.encoding)
# 查询网页响应状态
print(response.status_code)

# 获取网页html内容的有两种方式response.text 和 response.content.decode('utf-8')
# response.text 有python猜测网页的编码方式，可能尝试乱码，response.content.decode('utf-8')可以指定编码方式
print(response.text)

html_data = response.content.decode('utf-8')
print(html_data)
