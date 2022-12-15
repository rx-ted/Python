import requests
import re
from bs4 import BeautifulSoup
import json


# 得到url数据
def get_url(geturl, headers):
    response_get = requests.get(url=geturl, headers=headers)
    if response_get.status_code == 200:
        return response_get
    else:
        print('404!!!Fail to respond to network!')


# 响应并提交数据，得到url数据
def post(posturl, data, headers):
    response_post = requests.post(url=posturl, data=data, headers=headers)
    if response_post.status_code == 200:
        return response_post
    else:
        print('404!!!Fail to respond to network!')


# 保存或者读取文件
def save_path(path, mode, encoding, data):
    with open(path, mode=mode, encoding=encoding)as f:
        f.write(data)
        if mode == 'r' or 'rb':
            print('Success to open the data.Read the data...')
        elif mode == 'w' or 'wb':
            print('Success to write the data.Write the data...')
        else:
            print('fail to open or write the data.Please try it...')
    f.close()


# 定义要保存或者读取文件的位置
def define_path(mode):
    path = input('Please read or save the path :')
    if save_path(path=path, mode=mode, encoding='utf-8'):
        print('success!!!')
        return path
    else:
        return EOFError


# 定义正则表达式
def re_th(url, headers):
    # 获取网页数据
    response = get_url(geturl=url, headers=headers).text
    # 以thead结构开头爬取用bs4
    soup = BeautifulSoup(response, 'lxml')
    thead = soup.select('tblite_hh')
    # 获取全部文本符合条件的数据
    data_re = '<th><a id=".*" class=".*">(.*)</a></th>'
    data = re.findall(data_re, str(thead))
    return data


# 主要运行程序
def main():
    # 混合型
    url = 'http://fund.eastmoney.com/trade/hh.html'
    jjjz_url = 'http://fund.eastmoney.com/js/jjjz_gs.js?v=0.07126483280633811'
    # 协议头
    headers = {
        'Accept-Ranges': 'bytes',
        'Cache-Control': 'max-age=600',
        'Content-Encoding': 'gzip',
        'Content-Type': 'text/html',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': 'fund.eastmoney.com',
        'Referer': 'http://fund.eastmoney.com/trade/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5 Safari/537.36'
    }
    get_jjjz = get_url(geturl=jjjz_url, headers=headers).text
    jjjz_dm = re.findall('(\d{1,8})', get_jjjz)
    jjjz_mc = re.findall('[\u4e00-\u9fa5]+', get_jjjz)

    # for item in jjjz_dm:
    #     print(item)
    # for item in jjjz_mc:
    #     print(item)
    print(jjjz_dm)
    print(jjjz_mc)
    # print(re_th(url=url, headers=headers))


if __name__ == '__main__':
    main()
