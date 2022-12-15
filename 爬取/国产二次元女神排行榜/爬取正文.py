import requests

# 爬取的网站
url = "http://www.ttpaihang.com/vote/rankresult-1501.html"
# 模拟浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.17 Safari/537.36'
}
# ip代理
# ip_url = '183.230.179.164:8060'
proxies = {'http': '183.230.179.164:8060',
           }

# 爬取网站
req = requests.get(url=url, headers=headers, proxies=proxies)
# 储存为文本
req.encoding = 'gbk'
html = req.text
print((html))
# 储存
with open('ns.txt', 'w',encoding='utf-8')as f:
    f.write(html)
