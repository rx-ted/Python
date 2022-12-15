from lxml import etree
import requests
import os

path = 'D:\data'

for j in range(1, 20):
    url = 'http://m.umei.cc/meinvtupian/meinvxiezhen/203772.htm'
    if j > 1:
        url = url + '_' + str(j)
    # print(url)
    response = requests.get(url=url).content.decode('utf-8')
    # print(response)

    html = etree.HTML(response)
    lis = html.xpath('//*[@id="ArticleBox"]/p/a/img')
    i = 1
    for li in lis:
        src = li.get('src')
        alt = li.get('alt')
        print(src, alt)
        all_path = path + '\\' + alt
        # print(etree.tostring(lis, encoding='utf-8').decode('utf-8'))
        # 下载图片
        # 创建文件夹
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

        img = requests.get(url=src)
        if img.status_code == 200:
            with open(f'{All_path}{i}.jpg', 'wb')as f:
                f.write(img.content)
                print(alt, "下载成功!!!")
        else:
            print(url, "此网址不存在!!!")
        i += 1
