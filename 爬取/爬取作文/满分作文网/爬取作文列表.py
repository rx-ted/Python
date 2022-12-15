# Python版本：3.7.5

import requests
from lxml import etree
import re
url = 'http://www.zuowenwang.net/gaokao/'
url_0 = 'http://www.zuowenwang.net/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400'
}
text = requests.get(url=url, headers=headers)
text.encoding = "gbk"
html = etree.HTML(text.text)
uls = html.xpath("//ul[@class='tm_pageList']")[0]
for ul in uls:
    a_s = ul.xpath('//li/h3/a')

for a in a_s:
    a_title = a.get('title')
    a_href = a.get("href")
    a_href = url_0 + a_href
    if a_title != None:
        zw = requests.get(url=a_href, headers=headers)
        zw.encoding = "gbk"
        html_text = etree.HTML(zw.text)
        divs = html_text.xpath('//div[@class="article"]')[0]
        art = (etree.tostring(divs.xpath('//div[@class="article-t"]')[0], encoding='utf8').decode('utf8'))
        title_list = re.findall('h1>(.*)</h1>', art)
        writing_list = re.findall('div class="meta">(.*)</div', art)
        print(title_list[0] + '\n' + writing_list[0])
        content = (etree.tostring(divs.xpath('//div[@class="content"]')[0], encoding='utf8').decode('utf8'))
        article = re.findall('<p>(.*)</p>', content)
        with open(f'./作文列表/{title_list[0]}.txt', 'w')as fn:
            fn.write("")

        with open(f'./作文列表/{title_list[0]}.txt', 'a', encoding='utf-8')as fn:
            fn.write(title_list[0] + '\t' + writing_list[0] + '\n')

        for li in article:
            if True:
                with open(f'./作文列表/{title_list[0]}.txt', 'a', encoding='utf-8')as fn:
                    fn.write(li + '\n')
            else:
                print('Writing Error')
