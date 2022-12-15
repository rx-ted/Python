

import requests
from bs4 import BeautifulSoup
import re
import json
from lxml import etree
import os



url = 'http://zhainanba.net/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4021.2 Safari/537.36',
        'Host': 'zhainanba.net'
    }
response = requests.get(url=url, headers=headers).text
html = etree.HTML(response)
lis = html.xpath('/html/body/section/div/div/div[1]/ul/li/a')
hrefs = []
titles = []
for li in lis:
    # lis = (etree.tostring(li, encoding='utf-8').decode('utf-8'))
    href = li.get('href')
    title = li.get('title')
    hrefs.append(href)
    titles.append(title)
print(hrefs,titles)


