# 1、导入库
import re
import requests

# 2、定义url和请求头
url = 'https://s.weibo.com/top/summary'

# 定义请求头 
url = "https://s.weibo.com/top/summary/"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
           "cookie": "SUB=_2AkMUnjXgf8NxqwFRmP8WyWvjZY52zQzEieKiwsQ7JRMxHRl-yT9kqlE4tRB6Px4bDzSHkzvBITl5nmzLFI-JI2GggfEi; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWOgaE_-ubyxa7KFL77lwXu; _s_tentry=weibo.com; Apache=2054102635892.19.1673709436498; SINAGLOBAL=2054102635892.19.1673709436498; ULV=1673709436566:1:1:1:2054102635892.19.1673709436498:",
           }
# 3、发送请求，解码html
response = requests.get(url, headers = headers)

# 解码
content = response.content.decode('utf8')

# 4、使用正则表达式提取数据
# 	(1)获取热搜
contents = re.findall('<td class="td-02">.*?<a.*?>(.*?)</a>', content, re.DOTALL)[1:]
print(contents)
# 	(2)获取热度
hots = re.findall('<td class="td-02">.*?<span>(.*?)</span>', content, re.DOTALL)
print(contents)
print(hots)

# 5、存储数据
sinas = []
for cont,hot in zip(contents, hots):
    sina = {
        "content":cont,
        "hot":hot,
    }
    sinas.append(sina)
print(sinas)