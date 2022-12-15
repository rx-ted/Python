import requests
import urllib.parse
import  urllib.request
from bs4 import BeautifulSoup
import json
import re


def get_data(url):
    headers = {
        'referer': 'https://www.zhipin.com/web/common/security-check.html?seed=g03EO0YqfTLR%2B2HBljaTK%2FLxYMZUi5IAgqe5zvjxOe4%3D&name=5e1648a1&ts=1566976649055&callbackUrl=%2Fjob_detail%2F%3Fquery%3Dpython%26city%3D101010100%26industry%3D%26position%3D',
        #  ':path': '/job_detail/?query=python&city=101010100&industry=&position=',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400'
    }
    response0 = urllib.request.Request(url=url)
    response1 = urllib.request.urlopen(response0)
    html = response1.read().decode("utf-8")
    # print(html)
    soup = BeautifulSoup(html,'lxml')
    print(soup)



def get_url(url1, start_page, end_page):
    url0 = 'https://www.zhipin.com/c101010100/'
    for i in range(start_page, end_page):
        url = url0 + f'?query={url1}' + f'&page={i}' + f'ka=page-{i}'
        print(url)
        get_data(url)



if __name__ == '__main__':
    get_name = input("请输入你想要搜索的名字：")
    url1 = urllib.parse.quote(get_name)
    begin_page = int(input("默认首页："))
    end_page = int(input("默认末页："))
    get_url(url1, begin_page, end_page)

'''
数据分析：
①：https://www.zhipin.com/c101010100/?query=%E7%88%AC%E8%99%AB&page=3&ka=page-3
②：https://www.zhipin.com/c101010100/?query=%E7%88%AC%E8%99%AB&page=2&ka=page-2
    url0='https://www.zhipin.com/c101010100/'       # 源url
    url1='?query=%E7%88%AC%E8%99%AB'     # url编码   ->源：?query=爬虫  
        简化  url1= f'?query={搜索}' 
    url2='&page=2'      # 简化 url2 = f'&page={页数}'
    url3='&ka=page-2'       # 简化 url3 = f'ka=page-{页数}'
合并为：url = url0+url1+url2+url3

'''
