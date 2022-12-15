import requests
import sys
import io
from lxml import etree
import os


def build_new_field(new_field_path):
    #     # 创建文件夹
    isExists = os.path.exists(new_field_path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(new_field_path)
        print(new_field_path + ' 创建成功')
    else:
        # 如果目录存在则不创建，并提示目录已存在
            print(new_field_path + ' 目录已存在')


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

while True:
    # 得到网页数据
    response = requests.get(url, headers=headers).content.decode('utf-8')
    # 用lxml进行提取数据
    html = etree.HTML(response)
    lis = html.xpath('/html/body/div[4]/div/a')
    url_head = 'http://m.umei.cc/'
    field_path = 'd:\\data'  # 要保存文件夹位置
    for li in lis:
        href = li.get('href')
        title = li.get('title')
        # print(href,title)
        spelling_url = url_head + href  # 拼写网址头+爬取href等于完整网址
        # print(spelling_url)
        response1 = requests.get(url=spelling_url, headers=headers).content.decode('utf-8')
        html1 = etree.HTML(response1)
        lis1 = html1.xpath('/html/body/div[8]/ul/li/a')
        for li1 in lis1:
            href1 = li1.get('href')  # 爬取图片组网址
            alt = li1.xpath('./img')[0].get('alt')  # 爬取图片组标题
            src = li1.xpath('./img')[0].get('lazysrc')  # 爬取图片封面地址
            # print(alt, href1, src, "提取成功！")
            all_path = field_path + '\\' + alt  # 绝对地址+爬取alt（标题）
            build_new_field(new_field_path=all_path)
            # 打开已经新建文件夹并新建文件
            All_path = all_path + '\\'
            # print(All_path)
            # img = requests.get(url=src,headers=headers).content
            # with open(f'{All_path}封面.jpg', 'wb')as f:
            #   f.write(img)
            #  print("下载着……\t", alt, "\t下载成功!!!")
            for j in range(1,20):
                url1 = href1
                if j > 1:
                    url1 = url1[:-4] + '_' + str(j)+'.htm'
                print(url1)
                response2 = requests.get(url=url1).content.decode('utf-8')
                html = etree.HTML(response2)
                lis2 = html.xpath('//*[@id="ArticleBox"]/p/a/img')

                for li2 in lis2:
                    src1 = li2.get('src')  # 图片组里面的某一个网址
                    print(alt,j,src1)
                    img = requests.get(url=src1)
                    if img.status_code == 200:
                        with open(f'{All_path}{str(j)}.jpg', 'wb')as f:
                            f.write(img.content)
                            print(f"第{str(j)}张标题为{alt}的图片", "下载成功!!!")
                    else:
                        with open(f'{field_path}\\日志.txt', 'a+')as f:
                            f.writelines(f"错误记录：{j}, {alt}, {url1}, {src1}")
                            print(src1, "此网址不存在!!!")
