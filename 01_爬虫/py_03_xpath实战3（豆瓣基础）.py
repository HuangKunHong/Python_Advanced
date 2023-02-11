# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 20:54:06 2023

@author: Administrator
"""

# 1、导入必要的库或模块
import requests
from lxml import etree

# 2、定义网页和请求头
url = "https://movie.douban.com/review/1000369/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.52",
}

# 3、获取 html 页面（注意编码和转码的问题）
response = requests.get(url, headers = headers)
content = response.content.decode("utf8")

# 4、etree 解析
html = etree.HTML(content)


# 5、观察网页源码，查看标签特征
# 6、编写 xpath 语法，获取标签内容（文本信息末尾添加 / text()）
title = html.xpath('//div[@class="subject-title"]/a/text()')[0][2:]
commenter = html.xpath('//header/a/span/text()')[0]
rank = html.xpath('//header/span/@title')[0]
comment = html.xpath('//div[@class="review-content clearfix"]/p/text()')
# 合并列表内容（合并p标签）
comment = "".join(comment)



# 7、存储数据
review = {
    "电影名": title,
    "评论者": commenter,
    "评分": rank,
    "影评": comment,
}

print(review)