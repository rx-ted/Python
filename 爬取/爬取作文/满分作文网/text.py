# coding=utf-8

import requests

from lxml import etree

url = 'http://www.zuowenwang.net/gaokao/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400'
}
# 获取网页数据
text = requests.get(url=url, headers=headers)
# 转码
text = text.text.encode('ISO-8859-1').decode('gbk')

html = etree.HTML(text)

ul = html.xpath("//ul[@class='tm_pageList']")[0]

# print((etree.tostring(ul,encoding='utf8').decode('utf8')))

lis = ul.xpath('./li/h3/a')


for li in lis:
    # print((etree.tostring(li,encoding='utf8').decode('utf-8')))
    title = li.xpath('@href')[0]
    print((etree.tostring(title,encoding='utf-8').decode('utf8')))




# print()
# 以二进制保存
# res = text.content.decode('gbk').encode('utf-8')


#
# with open('writing.txt','wb')as f:
#     f.write(res)
