import requests
import sys
import io
from lxml import etree
import json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

url = 'http://m.umei.cc/tags/'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'Hm_lvt_19d597dda6fff717a20d276fa907bd17=1579874963,1579962492; Hm_lpvt_19d597dda6fff717a20d276fa907bd17=1579964664',
    'Host': 'm.umei.cc',
    # 'If-Modified-Since': 'Fri, 29 Nov 2019 12:07:51 GMT',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4021.2 Safari/537.36',
}
response = requests.get(url, headers=headers).content.decode('utf-8')
# print((response))

html = etree.HTML(response)
lis = html.xpath('/html/body/div[4]/div/a')
href_title = []
for li in lis:
    href = li.get('href')
    title = li.get('title')
    href_title.append(href + ';' + title)
# print(href_title)
with open('D:\\Users\\Administrator\\Desktop\\个人工作文件\\python项目\\爬取\\爬取图片\\优美图\\2.txt', 'w')as f:
    f.writelines('\n'.join(href_title))
f.close()
