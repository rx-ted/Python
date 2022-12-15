import os
import requests
from bs4 import BeautifulSoup
from lxml import etree  # 数据抽取

# url = f'https://www.mzitu.com/tag/ugirls/page/'

headers = {
    'referer': 'https://www.mzitu.com/tag/ugirls/',

    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36'
}

headers1 = {
        ':authority': 'www.mzitu.com',
    ':method': 'GET',
    ':path': '/tag/ugirls/',
    ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1566008387,1566012892; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1566019231',
    'if-modified-since': 'Sat, 17 Aug 2019 02:47:36 GMT',
                         'referer': 'https://www.mzitu.com/tag/ugirls/page/17/',
                       'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36'

}
path = 'images/'
if not os.path.exists(path=path):
    os.mkdir(path)

for page in range(1, 18):
    url = f'https://www.mzitu.com/tag/ugirls/page/{page}/'
    response = requests.get(url, headers=headers)

    # print(response.text)
    html = etree.HTML(response.text)
    ul = html.xpath("//ul[@id='pins']/li/a/img")

    # print(ul)
    for img in ul:
        img_url = img.get('data-original')
        img_name = img.get('alt')
        # print(img_name, img_url)
        response = requests.get(img_url, headers=headers)
        with open(f'images/{img_name}.jpg', 'wb') as f:
            print(img_name)
            f.write(response.content)

# response = requests.get(url, headers=headers)



