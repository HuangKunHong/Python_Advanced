import requests

# 登陆页面url
url = "https://accounts.douban.com/passport/login"

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54",
    
    }
# 账号密码
data = {
        "name": "18559258323",
        "password": "Kun089502"
        }

# 模拟登陆
session = requests.session()
session.post(url, data=data, headers=headers)

# 登陆成功
response = session.get("https://movie.douban.com/", headers=headers)
content = response.content.decode("utf-8")

with open("豆瓣电影.html", "w", encoding="utf-8") as f:
    f.write(content)