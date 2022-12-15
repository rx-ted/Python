import random
import requests
from lxml import etree

# 不可改的参数

# 目标网址
url = 'http://m.umei.cc/tags/'
# 请求头
user_agent_list = [
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0.6',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4021.2 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36']
UserAgent = random.choice(user_agent_list)
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'Hm_lvt_19d597dda6fff717a20d276fa907bd17=1579874963,1579962492; Hm_lpvt_19d597dda6fff717a20d276fa907bd17=1579964664',
    'Host': 'm.umei.cc',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': UserAgent
}
urlHead = 'http://m.umei.cc/'
saveField_path = 'd:\\data'  # 要保存文件夹位置


def Geturl_data():
    # 得到网页数据
    response = requests.get(url, headers=headers).content.decode('utf-8')
    # 用lxml进行提取数据
    html = etree.HTML(response)
    lis = html.xpath('/html/body/div[4]/div/a')
    for li in lis:
        href = li.get('href')
        title = li.get('title')
        print(href, title)
        spelling_url = urlHead + href  # 拼写网址头+爬取href等于完整网址
        print(title, spelling_url, headers)



Geturl_data()
