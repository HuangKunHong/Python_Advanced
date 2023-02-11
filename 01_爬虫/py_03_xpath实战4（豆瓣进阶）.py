import requests
from lxml import etree

# 1、获取共计 5页的 所有url ；
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}

urls = []
for i in range(5):
    i = i * 20
    url = f"https://movie.douban.com/review/best/?start={i}"
    urls.append(url)

# 2、遍历每一页的 url ，从每页中得到所有的 a标签下的 href 属性；
review_urls = []
for url in urls:
    response = requests.get(url, headers = headers)
    content = response.content.decode('utf8')
    html = etree.HTML(content)
    review_url = html.xpath('//h2/a/@href')
    review_urls.append(review_url)

reviews = []
i = 0
# 3、将 href 中的链接按上节课内容，将所有关于影评爬 取下来。
for review_url in review_urls:
    for review in review_url:
        try:
            # # 1、导入必要的库或模块
            # import requests
            # from lxml import etree
    
            # 2、定义网页和请求头
            # url = "https://movie.douban.com/review/1000369/"
            # headers = {
            #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.52",
            # }
    
            # 3、获取 html 页面（注意编码和转码的问题）
            response = requests.get(review, headers = headers)
            content = response.content.decode("utf8")
    
            # 4、etree 解析
            html = etree.HTML(content)
    
    
            # 5、观察网页源码，查看标签特征
            # 6、编写 xpath 语法，获取标签内容（文本信息末尾添加 / text()）
            title = html.xpath('//div[@class="subject-title"]/a/text()')[0][2:]
            commenter = html.xpath('//header/a/span/text()')[0]
            rank = html.xpath('//header/span/@title')
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
            reviews.append(review)
        except:
            continue
    
    i += 1    
    print(f'第{i}页已爬取完成')
        

