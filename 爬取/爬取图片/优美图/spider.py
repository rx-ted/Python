import requests
import sys
import io
from lxml import etree
import os

print('Python %s on %s' % (sys.version, sys.platform))

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# 目标网址
url = 'http://m.umei.cc/tags/'

# 请求头
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'Hm_lvt_19d597dda6fff717a20d276fa907bd17=1579874963,1579962492; Hm_lpvt_19d597dda6fff717a20d276fa907bd17=1579964664',
    'Host': 'm.umei.cc',

    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4021.2 Safari/537.36',
}
# 得到网页数据
response = requests.get(url, headers=headers).content.decode('utf-8')
# 用lxml进行提取数据
html = etree.HTML(response)
lis = html.xpath('/html/body/div[4]/div/a')
href_title = []
path = 'D:\data'
for li in lis:
    href = li.get('href')
    title = li.get('title')
    #     href_title.append(href + ';' + title)
    # # print(href_title)
    # with open('D:\\data\\tags.txt', 'w')as f:
    #     f.write('\n'.join(href_title))
    # f.close()

    response1 = requests.get(url, headers=headers).content.decode('utf-8')
    html = etree.HTML(response1)
    lis1 = html.xpath('/html/body/div[8]/ul/li/a')

    i = 0

    href_alt = []
    lazysrc = []
    for li1 in lis1:
        href = li1.get('href')
        alt = li1.xpath('./img')[0].get('alt')
        src = li1.xpath('./img')[0].get('lazysrc')
        print(alt, href, src, "提取成功！")
        # href_alt.append(href + '❤' + alt)
        # lazysrc.append(src)

        # for li in href_alt:
        #     alt = (li.split('❤')[1])
        all_path = path + '\\' + alt
        #     # 创建文件夹
        isExists = os.path.exists(all_path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(all_path)
            print(all_path + ' 创建成功')
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print(all_path + ' 目录已存在')
        All_path = all_path + '\\'
        img = requests.get(url=lazysrc[i]).content
        with open(f'{All_path}封面.jpg', 'wb')as f:
            f.write(img)
            print(alt, "下载成功!!!")
        i = i + 1
        # print(href_alt)
