import urllib.request
from bs4 import BeautifulSoup
import re

main_url = 'https://book.douban.com/chart?subcat=F'

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3941.4 Safari/537.36"
}
url = urllib.request.Request(url=main_url, headers=headers)
proxies = {"http": "183.230.179.164:8060"}
hander = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(hander)
resp = opener.open(url)
html = resp.read().decode('utf-8')
soup = BeautifulSoup(html, 'lxml')
# 爬取封面,且网址
covers = soup.select('#content > div > div.article > ul > li > div.media__img > a')
information = soup.select('#content > div > div.article > ul > li > div.media__body')
# title = re.findall('<a class="fleft" href=".*">(.*)</a>', str(information))
book_data = []
for cover in covers:
    href = re.findall('<a href="(.*)">', str(cover))
    img_href = re.findall('<img .* src="(.*)"/></a>', str(cover))
    re_info = '''(.*)'''
    info = re.findall(re_info,str(information))
    print(info)

    # book_data.append(href+img_href+info+grade+price)
print(book_data)

'''
<p class="clearfix w250">(.*)</p>
'''
