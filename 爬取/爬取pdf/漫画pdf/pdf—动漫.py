'''
re:正则表达式
lxml:xpath
bs4：BeautifulSoup > 解析网页的速速慢
selector
pyquery

爬虫+图像处理

网址：https%3a%2f%2fmhpic.manhualang.com%2fcomic%2fZ%2f%e9%81%ae%e5%a4%a9%e6%8b%86%e5%88%86%e7%89%88%2f%e7%ac%ac2%e8%af%9d%2f1.jpg-mht.middle.webp
     https%3a%2f%2fmhpic.manhualang.com%2fcomic%2fZ%2f%e9%81%ae%e5%a4%a9%e6%8b%86%e5%88%86%e7%89%88%2f%e7%ac%ac1%e8%af%9d%2f1.jpg-mht.middle.webp
     https%3a%2f%2fmhpic.manhualang.com%2fcomic%2fZ%2f%e9%81%ae%e5%a4%a9%e6%8b%86%e5%88%86%e7%89%88%2f%e7%ac%ac10%e8%af%9d%2f1.jpg-mht.middle.webp


    https://www.manhuatai.com/zhetian/265.html

'''

import requests
from lxml import etree
from PIL import Image
from io import BytesIO

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400'
}

# url = 'https://mhpic.manhualang.com/comic/Z/%E9%81%AE%E5%A4%A9%E6%8B%86%E5%88%86%E7%89%88/%E7%AC%AC1%E8%AF%9D/4.jpg-mht.middle.webp'


root = 'https://www.manhuatai.com/henchunhenaimei/'
response = requests.get(root)
# print(response.text)

html = etree.HTML(response.text)
lis = html.xpath("//ol[@id='j_chapter_list']/li/a/div/img/@data-src")

imgs = []
count = 0

for li in lis:
    # print(li)
    li = li.replace("cnmanhua", "manhualang")
    li.strip(".jpg-300x1502")
    print(li)
    index = 0
    while True:

        # url = "https:"+"//mhpic.manhualang.com/comic/Z/遮天拆分版/第1话/1.jpg-300x150.jpg"
        url = f'https:{li}{index}.jpg-mnt.middle.webp'
        print(url)
        index += 1
        resp = requests.get(url)
        if resp.content.startswith(b"<?xml"):  # 不是图片
            break
        im = Image.open(BytesIO(resp.content))
        # im.show()
        imgs.append(im)
    if count > 10:
        break
    count += 1

imgs[0].save("pdf/遮天.pdf", save_all=True, append_images=imgs[1:])

# with open('pdf/a.jpg','wb')as f:
#     f.write(response.content)
