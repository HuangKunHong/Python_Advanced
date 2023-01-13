# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests

# http常见请求：GET POST

# 访问的网页地址
url = "https://user.qzone.qq.com/1241335400"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54",
    "Cookie": "pgv_pvid=8027295972; RK=w2XYBhMBb4; ptcz=b24ef4f591d18bd31b04fe2ad60a76c11ced2ffa03a60992e33e7bb8fa8ef41d; Qs_lvt_323937=1663511865; Qs_pv_323937=3273272887043555300; tvfe_boss_uuid=51cbc5b4f56c85f3; fqm_pvqid=aadbcfbc-ed3b-4292-b69a-f3badc9379e1; ptui_loginuin=1241335400; o_cookie=1241335400; pac_uid=1_1241335400; _qpsvr_localtk=0.2581292139197726; pgv_info=ssid=s3768415565; uin=o1241335400; skey=@YUe3DvRLr; p_uin=o1241335400; pt4_token=UV1QzRdIrZhT125XutdrSUKkOwjC5hfpBUs-IAn23is_; p_skey=uWAnSMmAuYszj7329X-eilbiDgXjxUKp9qEKRbEqn*k_; Loading=Yes; x-stgw-ssl-info=d87e786bccfb6f6a3045a63343be2968|0.096|-|1|.|Y|TLSv1.2|ECDHE-RSA-AES128-GCM-SHA256|21500|h2|0",

    
    }
# 响应
response = requests.get(url, headers=headers)
html_data = response.content.decode('utf-8')

with open("QQ空间.html", "w", encoding="utf-8") as f:
    f.write(html_data)