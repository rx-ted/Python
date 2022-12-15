import urllib.request
import re
from bs4 import BeautifulSoup

electron_url = 'https://book.douban.com/chart?subcat=F'
paper_url = 'https://book.douban.com/chart?subcat=I'


# 书的形式，有2种：电子版、纸质版
def choose_form_book():
    while True:
        i = int(input("请选择书的形式：\n1.电子版\n2.纸质版\n请输入序号:\t"))
        if i == 1:
            main_url = electron_url
            print("电子版网址:", electron_url)
            return main_url

        elif i == 2:
            main_url = paper_url
            print("电子版网址:", paper_url)
            return main_url

        else:
            print("请输入正确的序号！")


def get_url(main_url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3941.4 Safari/537.36"
    }
    url = urllib.request.Request(url=main_url, headers=headers)
    proxies = {"http": "183.230.179.164:8060"}
    hander = urllib.request.ProxyHandler(proxies=proxies)
    opener = urllib.request.build_opener(hander)
    resp = opener.open(url)
    html = resp.read().decode('utf-8')
    soup = BeautifulSoup(html,'lxml')
    # 爬取封面
    covers = soup.select('#content > div > div.article > div.section.popular-books > div.bd > ul > li')
    for cover in covers:
        print(cover)

if __name__ == '__main__':
    main_url = choose_form_book()
    get_url(main_url)
