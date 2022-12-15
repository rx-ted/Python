import requests
from lxml import etree
url = 'http://www.zuowenwang.net/gaokao/'
url_0 = 'http://www.zuowenwang.net/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400'
}
text = requests.get(url=url, headers=headers)

text.encoding = "gbk"

html = etree.HTML(text.text)

# print((etree.tostring(html,encoding='utf8').decode('utf8')))
title = []
href = []
uls = html.xpath("//ul[@class='tm_pageList']")[0]
for ul in uls:
    # print((etree.tostring(ul, encoding='utf8').decode('utf8')))
    a_s = ul.xpath('//li/h3/a')

for a in a_s:
    a_title = a.get('title')
    a_href = a.get("href")
    a_href = url_0 + a_href
    if a_title != None:
        title.append(a_title)
        href.append(a_href)
        print(a_title, a_href)

    # zw = requests.get(url=a_href, headers=headers)
    # zw.encoding = "gbk"
    #
    # html_text = etree.HTML(zw.text)
    # print((etree.tostring(html_text,encoding='utf8').decode('utf8')))

# print(title)
# print(href)

