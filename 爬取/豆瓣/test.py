import requests
from lxml import etree
from bs4 import BeautifulSoup

open_url='https://movie.douban.com/cinema/nowplaying/beijing' # 正在上映
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4343.0 Safari/537.36'
}

res = requests.get(open_url).text


print(res)
soup = BeautifulSoup(res,'lxml')
items = soup.select('ul')
print(items)