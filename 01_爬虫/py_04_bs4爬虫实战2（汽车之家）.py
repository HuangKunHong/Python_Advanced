import requests
from bs4 import BeautifulSoup

# 2、定义 url 和请求头参数
url = 'https://www.autohome.com.cn/news/'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    }




# 定义url
urls = []
for i in range(6):
    url = f'https://www.autohome.com.cn/news/{i}/#liststart'
    urls.append(url)


news = []
# 遍历所有url
for url in urls:
    try:
        # 发送请求
        response = requests.get(url, headers=headers)
        content = response.content.decode('gbk')
        # print(content)

        # 4、实例化 BeautifulSoup 对象（中介）
        soup = BeautifulSoup(content, 'lxml')
        # print(soup)
        
        # 5、获取数据
        divs = soup.find_all('div', class_='article-wrapper')
        # print(divs)
        for div in divs:
            titles = div.find_all('h3')
            times = div.find_all('span', class_="fn-left")
            profiles = div.find_all('p')

            for title,time,profile in zip(titles, times, profiles):
                title = title.string
                time = time.string
                profile =profile.string

                car_news = {
                    '标题': title,
                    '时间': time,
                    '文章': profile, 
                }

                news.append(car_news)
    except:
        continue

print(news)

# 6、存储数据

