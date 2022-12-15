from lxml import etree
import requests
import os

url = 'https://m.umei.cc/tags/xnjedtlqll.htm'

headers = {
    'Request URL': 'https://m.umei.cc/tags/xnjedtlqll.htm',
    'content-type': 'text/html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

response = requests.get(url, headers=headers).content.decode('utf-8')
# print(response)
html = etree.HTML(response)
# /html/body/div[8]/ul/li/a/img
# /html/body/div[8]/ul/li/a
lis = html.xpath('/html/body/div[8]/ul/li/a')
i = 0
href_alt = []
lazysrc = []
for li in lis:
    # print(etree.tostring(li, encoding='utf-8').decode('utf-8'))
    href = li.get('href')
    alt = li.xpath('./img')[0].get('alt')
    src = li.xpath('./img')[0].get('lazysrc')
    href_alt.append(href + '❤' + alt)
    lazysrc.append(src)

# print(href_alt)
i = 0
path = 'D:\data'

for li in href_alt:
    alt = (li.split('❤')[1])
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
    All_path = all_path+'\\'
    img = requests.get(url=lazysrc[i]).content
    with open(f'{All_path}封面.jpg', 'wb')as f:
        f.write(img)
        print(alt, "下载成功!!!")
    i = i + 1
print(href_alt)
