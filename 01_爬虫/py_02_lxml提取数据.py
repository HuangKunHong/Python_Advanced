# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 23:05:54 2023

@author: Administrator
"""

from lxml import etree

"""
1. 读取HTML字符串
"""

text = \
    """
<tr class = "hots">
    <td class = "1">hot1</td>
    <td class = "2">hot2</td>
    <td class = "3">hot3</td>
    <td class = "4">hot4</td>
    <td class = "5">hot5</td>
    <td class = "6">爬虫</td>
</tr>
    """
print(text)

# 现在text是字符串数据，xpath不能直接解析
# 利用etree.HTML将字符串解析为HTML文档
html = etree.HTML(text)
print(html)

# 目前html是一个Element html类型数据，直接print，打印的是内存地址
# 如果想要打印html的内容，需要用etree.tostring 转化为字符串数据
# 转换后是 bytes流数据，为了在使用代码的过程中正常显示中文，同时需要字符串进行了编码的转换和解析。
result = etree.tostring(html, encoding="utf8").decode("utf8")
print(result)

"""
2. 直接解析html文件
"""

# 利用parse导入测试文件进行解析
html =etree.parse(r"D:\Users\Administrator\Desktop\Python 学习\Python_Advanced\01_爬虫\实例文件\test.html")
result = etree.tostring(html, encoding="utf8").decode("utf8")
print(result)


"""
2. 解析直接从网页另存为的html文件
"""

# 默认使用的xml解析器，直接解析另存为的html文件，很可能解析错误，这时候需要自定义解析器
# 自定义一个解析器
parser = etree.HTMLParser(encoding="utf8")
html =etree.parse(r"D:\Users\Administrator\Desktop\Python 学习\Python_Advanced\01_爬虫\实例文件\baidu.html"
                  , parser = parser)
result = etree.tostring(html, encoding="utf8").decode("utf8")
print(result)