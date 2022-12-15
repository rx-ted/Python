import requests

from lxml import etree
import re

a_href = 'http://www.zuowenwang.net//p/19907.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400'
}

zw = requests.get(url=a_href, headers=headers)
zw.encoding = "gbk"

html_text = etree.HTML(zw.text)
# print((etree.tostring(html_text,encoding='utf8').decode('utf8')))

divs = html_text.xpath('//div[@class="article"]')[0]
# print((etree.tostring(divs, encoding='utf8').decode('utf8')))
# content = divs.xpath('//div[@class="content"]')[0]


art = (etree.tostring(divs.xpath('//div[@class="article-t"]')[0], encoding='utf8').decode('utf8'))
title_list = re.findall('h1>(.*)</h1>', art)
writing_list = re.findall('div class="meta">(.*)</div', art)

content = (etree.tostring(divs.xpath('//div[@class="content"]')[0], encoding='utf8').decode('utf8'))
article = re.findall('<p>(.*)</p>', content)

print(title_list[0] + '\n' + writing_list[0])

with open(f'./作文列表/{title_list[0]}.txt', 'a', encoding='utf-8')as fn:
    fn.write(title_list[0] + '\n' + writing_list[0]+'\n')

for li in article:
    if True:
        with open(f'./作文列表/{title_list[0]}.txt', 'a', encoding='utf-8')as fn:
            fn.write(li+'\n')
    else:
        print('Writing Error')