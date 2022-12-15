import requests
import re
from lxml import etree
import random
import chardet
# import StringIO
import gzip


def geturl():
    proxies = [
        "https://112.87.71.162:9999",
        "https://125.123.139.163:9999",
        "https://116.209.55.229:9999",
        "https://104.248.99.101:3128",
        "https://116.209.52.240:9999",
        "https://116.192.171.51:31742",
        "https://113.121.146.70:9999",
        "https://112.85.129.166:9999",
        "https://1.10.188.100:59164",
    ]
    headers = {
        'Connection': 'keep-alive',
        'Content-Encoding': 'gzip',
        'Content-Type': 'text/html; charset=utf-8',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
        'Remote Address': '120.77.130.244:80',
        'Vary': 'Accept-Encoding'
    }
    proxy = random.choice(proxies)
    # 拼字
    my_proxy = {"https": proxy}
    # print(my_proxy)
    url = 'http://huodong.myzaker.com/h/2019ncov/map.php?need_user_info=Y'
    # response.encoding = 'utf-8'
    text = requests.get(url=url, headers=headers).content.decode('utf-8')
    html = etree.HTML(text)
    # print((etree.tostring(html,encoding='utf8').decode('utf8')))
    # /html/body/div[1]/div[2]/div[2]
    lis = html.xpath('/html/body/div[1]/div')
    for li in lis:
        print(etree.tostring(li, encoding='utf-8').decode('utf-8'))

    # with open('data.png', 'wb')as f:
    #     f.write(html)
    # f.close()


geturl()
