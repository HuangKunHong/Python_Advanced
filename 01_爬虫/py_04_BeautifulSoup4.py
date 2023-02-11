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

# 1. 导入模块
from bs4 import BeautifulSoup

# 2. 实例化BeautifulSuop对象
soup = BeautifulSoup(text, 'lxml')

"""
获取所有的div标签
"""

divs = soup.find_all('div')
print(divs)
# bs4提取的结果不是列表，但使用print打印时
# 输出的结果是一个列表，每一个div作为列表中的一个元素
print(type(divs))

for div in divs:
    print(div)
    print("*" * 50)
    
"""
获取指定的div标签
"""
# 获取第二个div
div = soup.find_all('div')[1]
print(div)
print(type(div))

div = list(soup.find_all('div')[1])
print(div)
print(type(div))

# 获取第二个到第十个div
divs = soup.find_all('div')[1:10]
print(div)
print(type(div))
for div in divs:
    print(div)
    print("*" * 50)
    
"""
3 获取拥有指定属性的标签（id = even的div标签）
"""
# 方法1
divs = soup.find_all('div', id='even')
for div in divs:
    print(div)
    print("*" * 50)
    
# 方法2
divs = soup.find_all('div', attrs = {'id' :'even'})
for div in divs:
    print(div)
    print("*" * 50)

"""
4 获取拥有多个指定属性的标签（class="position" width="350"的span标签）
"""
# 方法一
span = soup.find_all('span', class_="position", width="350")
print(span)

# 方法二
span = soup.find_all('span', attrs ={"class":"position", "width":"350"})
print(span)


"""
5 获取标签的属性值
"""
alist = soup.find_all('a')

# 方法一：通过下标方式提取
for a in alist:
    href = a['href']
    print(href)
    

# 方法二：利用attrs参数提取
for a in alist:
    href = a.attrs["href"]
    print(href)
    
"""
6 获取所有的职位信息
"""

# 方法一
works = []
divs = soup.find_all('div')[1:]

for div in divs:
    # 获取职位信息
    a = div.find_all('a')[0]
    position = a.string
    
    # 职位信息
    category = div.find_all('span')[1].string
    
    # 获取人数
    nums = div.find_all('span')[2].string
    
    # 获取地区
    area = div.find_all('span')[3].string
    
    # 获取时间
    time = div.find_all('span')[4].string
    
    print(position, category, nums, area, time)
    
    positions = {
        "职位": position,
        "职位类别": category,
        "人数": nums,
        "地区": area,
        "时间": time,
        }
    
    works.append(positions)
    
print(works)

# 方法二
divs = soup.find_all('div')[1:]
for div in divs:
    infos = list(div.strings)
    print(infos)
    
# 去除列表中换行符的方法
divs = soup.find_all('div')[1:]
for div in divs:
    infos = list(div.stripped_strings)
    print(infos)
