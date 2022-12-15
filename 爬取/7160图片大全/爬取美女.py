import requests
import random
import urllib.request
import re

mn_url = 'https://www.7160.com/rentiyishu/56954/index.html'

proxies = (
    '182.35.86.239:9999', '113.128.31.218:32875', '120.83.96.225:9999', '117.95.174.34:9999', '114.239.250.102:9999',
    '117.88.176.110:3000', '124.237.83.14:53281', '61.128.208.94:3128')
proxy = random.choice(proxies)

proxy_ip = {"http:": proxy}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17'
}

httpproxy_handler = urllib.request.ProxyHandler(proxy_ip)
urllib.request.build_opener(httpproxy_handler)
res = requests.get(mn_url)
res = res.text.encode('ISO-8859-1').decode('gbk')

# print(res)
img_url_re = '''<li><a href=".*" title=".*"><img src="(.*)" alt="(.*)"><br>'''
img_urls = re.findall(img_url_re, res)
print(img_urls)

for img_url in img_urls:
    img = requests.get(url=img_url[0], headers=headers)
    try:
        with open(('./images/{}.jpg').format(img_url[1]), 'wb')as fp:
            fp.write(requests.get(url=img_url[0]).content)
    except:
        with open(('./images/{}.jpg').format(img_url[1]), 'wb')as fp:
            fp.write(requests.get(url="http:" + img_url[0]).content)
