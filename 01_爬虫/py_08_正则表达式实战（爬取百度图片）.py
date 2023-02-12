import requests
import re
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# 设置请求头
# headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41",
#
#             }
# url = "https://bkimg.cdn.bcebos.com/pic/48540923dd54564eaac98f02bede9c82d1584f58"
# # 发送get请求
# response = requests.get(url, headers = headers)
#
# # 变为byte流数据
# content = response.content
# # print(content)
#
# # 保存图片
# # w:write b:byte
# with open('tomato.jpg', 'wb') as f:
#     f.write(content)


#############################################
pic = input("请输入你需要爬取图片的关键词：")
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41",
            "Cookie": 'BDIMGISLOGIN=0; winWH=%5E6_1366x617; BDqhfp=%E7%8C%AA%E7%8C%AA%26%260-10-1undefined%26%260%26%261; BIDUPSID=05FF5174FA8E47BBF25B40C99834543B; PSTM=1653308192; BAIDUID=CD0C46452F6246B98F28F9CE51DF140C:SL=0:NR=10:FG=1; BAIDUID_BFESS=CD0C46452F6246B98F28F9CE51DF140C:SL=0:NR=10:FG=1; ZFY=ZCwiTFUJBHqk6zluuOAZj7Bx1WTcPt:BasE5qW3llb8k:C; BDUSS=RtbnV0cEVaNFRKVmxaM2NtSm02dzR6VkxGZH5OakYwQmVwckhKNDlTc014ZjFqSVFBQUFBJCQAAAAAAAAAAAEAAAC3361JSHVhbmdLdW5Ib20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAw41mMMONZjdW; BDUSS_BFESS=RtbnV0cEVaNFRKVmxaM2NtSm02dzR6VkxGZH5OakYwQmVwckhKNDlTc014ZjFqSVFBQUFBJCQAAAAAAAAAAAEAAAC3361JSHVhbmdLdW5Ib20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAw41mMMONZjdW; BAIDU_WISE_UID=wapp_1675917278658_706; RT="z=1&dm=baidu.com&si=85b4b750-7bbf-48f3-813c-fa7e0761d284&ss=ldwp4fp7&sl=3&tt=25z&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=36q&cl=2l3"; BA_HECTOR=84a4008h0h2l8k202l8181ap1hufetu1k; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=3; delPer=0; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; firstShowTip=1; cleanHistoryStatus=0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDRCVFR[tox4WRQ4-Km]=mk3SLVN4HKm; indexPageSugList=%5B%22%E7%95%AA%E8%8C%84%22%2C%22%E7%8C%AA%E7%8C%AA%22%2C%22%E5%9C%9F%E8%B1%86%22%2C%22%E6%9D%8E%E6%B1%87%E9%A2%96%22%2C%22%E9%BB%84%E5%9D%A4%E5%AE%8F%22%2C%22%E7%BD%91%E5%AE%89logo%22%2C%22wadd%22%2C%22%E7%8C%AAlogo%22%5D; H_PS_PSSID=36547_37557_38105_38091_38057_38116_38151_37989_37802_37921_38088_37900_26350_37958_38008_37881; userFrom=null',
            'Connection': 'close'
            }
url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1676134973089_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width"

kw = {
    "word": pic
}
response = requests.get(url, headers = headers, params=kw)
content = response.content.decode('utf8')

# 数据提取
detail_urls = re.findall('"objURL":"(.*?)"', content, re.DOTALL)
# print(detail_urls)

# 图片下载
i = 1
for detail_url in detail_urls:
    try:
        print(f"第{i}张图片正在下载")
        response = requests.get(detail_url, headers=headers)
        content = response.content
        path = r"./百度图片"
        if detail_url[-3:] == "jpg":
            with open(f'{path}/{i}.jpg', 'wb') as f:
                f.write(content)
        elif detail_url[-3:] == "jpeg":
            with open(f'{path}/{i}.jpeg', 'wb') as f:
                f.write(content)
        elif detail_url[-3:] == "png":
            with open(f'{path}/{i}.png', 'wb') as f:
                f.write(content)
        elif detail_url[-3:] == "bmp":
            with open(f'{path}/{i}.bmp', 'wb') as f:
                f.write(content)
        else:
            continue
        i += 1
    except:
        continue
print("所有爬取的图片已下载")
