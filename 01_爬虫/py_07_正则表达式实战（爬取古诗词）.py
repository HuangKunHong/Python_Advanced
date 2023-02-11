# 1、导入库
import requests
import re

# 2、定义请求头
headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
           }

# 3、分析 URL 的特点，批量获取
urls = []
for i in range(1, 5):
    url = f"https://www.gushiwen.cn/default_{i}.aspx"
    urls.append(url)
# print(urls)


i = 0
# 4、逐页获取 html 字符串
for url in urls:
    
    response = requests.get(url, headers = headers)
    content = response.content.decode('utf8')
    # print(content)
    # break
# 5、根据标签，使用正则表达式获取数据：获取标题，作者，朝代，诗文内容
    titles = re.findall('<b>(.*?)</b>', content, re.DOTALL)
    dynasties = re.findall('<p class="source">.*?<a.*?>(.*?)</a>', content, re.DOTALL)
    authors = re.findall('<p class="source">.*?<a.*?<a.*?>(.*?)</a>', content, re.DOTALL)
    poems = re.findall('<div class="contson".*?>(.*?)</div>', content, re.DOTALL)
    # print(titles,dynasties, authors, poems)
    # break

    new_poems = []
    gushici = []
    for poem in poems:
        new_poem = re.sub('<.*?>', "", poem)
        new_poem = new_poem.strip()
        new_poems.append(new_poem)
        print(titles,dynasties, authors, new_poems)
    

# 6、存储数据
    for title, dynasty, author, new_poem, in zip(titles, dynasties, authors, new_poems):
        poem = {
            "title":title,
            "dynasty":dynasty,
            "poem":new_poem,
        }
        gushici.append(poem)
    i += 1
    print(gushici)
    print(f"第{i}页已经爬取成功")
   