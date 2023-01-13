# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 23:52:48 2023

@author: Administrator
"""

from lxml import etree

text = \
"""
<ul class="ullist" padding="1" spacing="1">
    <li>
        <div id="top">
            <span class="position" width="350">职位名称</span>
            <span>职位类别</span>
            <span>人数</span>
            <span>地点</span>
            <span>发布时间</span>
        </div>
        <div id="even">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=33824&amp;keywords=python&amp;tid=87&amp;lid=2218">python开发工程师</a>
            </span>
            <span>技术类</span>
            <span>2</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="odd">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=29938&amp;keywords=python&amp;tid=87&amp;lid=2218">python后端</a>
            </span>
            <span>技术类</span>
            <span>2</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="even">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=31236&amp;keywords=python&amp;tid=87&amp;lid=2218">高级Python开发工程师</a>
            </span>
            <span>技术类</span>
            <span>2</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="odd">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=31235&amp;keywords=python&amp;tid=87&amp;lid=2218">python架构师</a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="even">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=34531&amp;keywords=python&amp;tid=87&amp;lid=2218">Python数据开发工程师</a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="odd">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=34532&amp;keywords=python&amp;tid=87&amp;lid=2218">高级图像算法研发工程师</a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="even">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=31648&amp;keywords=python&amp;tid=87&amp;lid=2218">高级AI开发工程师</a>
            </span>
            <span>技术类</span>
            <span>4</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="odd">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=32218&amp;keywords=python&amp;tid=87&amp;lid=2218">后台开发工程师</a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="even">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=32217&amp;keywords=python&amp;tid=87&amp;lid=2218">Python开发（自动化运维方向）</a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="odd">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=34511&amp;keywords=python&amp;tid=87&amp;lid=2218">Python数据挖掘讲师 </a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
    </li>
</ul>
"""

# 解析html字符串成HTML
html = etree.HTML(text)

# 1. 获取所有的div标签【节点选取】
# divs = html.xpath('//div')
# print(divs)

# for div in divs:
#     d = etree.tostring(div, encoding='utf8').decode('utf8')
#     print(d)
#     print("*" * 50)

# 2.获取指定的某个 div 标签 【 谓语的使用 】
div = html.xpath('//div[1]')[0]
DIV = etree.tostring(div, encoding='utf8').decode('utf8')
print(DIV)

# 3.获取所有的 id='even' 的 div 标签
divs = html.xpath('//div[@id = "even"]')
for div in divs:
    d = etree.tostring(div, encoding='utf8').decode('utf8')
    print(d)
    print("*" * 50)

# 4.获取标签的某个属性值
divs = html.xpath('//div/@id')
print(divs)

hrefs = html.xpath('//a/@href')
print(hrefs)


#5.获取 div 里面所有的职位信息
divs = html.xpath('//div')[1:]
works = []
for div in divs:
    work = {} # 新建一个空字典
    # 获取href
    url = div.xpath('.//a/@href')[0]
    # 获取a标签的文本信息
    position = div.xpath('.//a/text()')[0]
    # 获取工作类型
    work_type = div.xpath('.//span[2]/text()')[0]
    # 获取人数
    work_num = div.xpath('.//span[3]/text()')[0]
    # 获取工作地点
    area = div.xpath('.//span[4]/text()')[0]
    # 获取发布的时间
    time = div.xpath('.//span[5]/text()')[0]
    
    work = {
        "url":url,
        "position":position,
        "work_type": work,
        "work_num":work_num,
        "area":area,
        'time':time,}
    
    works.append(work)
 
print(works)